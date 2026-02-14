from typing import List, Optional
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup
from playwright.sync_api import Browser, sync_playwright

from interfaces.i_scraper import IScraperProvider
from logs.logger_singleton import Logger


class PlaywrightWebScraper(IScraperProvider):
    """
    Playwright scraper.

    Responsibilities:
    - Handle dynamic JavaScript-rendered pages
    - Extract internal links
    - Extract main text content
    """

    def __init__(self, timeout: int = 10000, base_url=str, logger=None):
        """
        Initialize scraper configuration.

        Args:
            Timeout in milliseconds
            Base URL for link extraction
            logger (Logger, optional): A logger instance. If None, a default logger is created using the class name.
        """
        self.timeout = timeout
        self._playwright = None
        self._browser: Browser | None = None
        self.logger = logger or Logger(self.__class__.__name__)
        self.base_url = base_url
        self.links: List[str] = []
        self.content: Optional[str] = None

    def fetch_links(self) -> List[str]:
        """
        Extract all valid internal links from a webpage.

        Returns:
            List[str]: A list of unique internal URLs found on the page.
        """
        links = set()
        self.logger.info(f"Fetching links from: {self.base_url}")

        try:
            with sync_playwright() as p:
                # Launch headless Chromium
                browser = p.chromium.launch(headless=True)
                page = browser.new_page()

                try:
                    # Go to the base URL and wait until network is idle
                    page.goto(self.base_url, timeout=self.timeout)
                    page.wait_for_load_state("networkidle")
                except Exception as e:
                    self.logger.error(f"Timeout loading page: {self.base_url} | {e}")
                    return []

                # Get fully rendered HTML
                html = page.content()
                soup = BeautifulSoup(html, "html.parser")

                base_domain = urlparse(self.base_url).netloc

                for tag in soup.find_all("a", href=True):
                    href = tag["href"].strip()

                    # Skip empty, mailto, tel, and anchor links
                    if not href or href.startswith(("mailto:", "tel:", "#")):
                        self.logger.warning(f"Skipping invalid link: {href}")
                        continue

                    # Convert relative to absolute
                    absolute = urljoin(self.base_url, href)
                    parsed = urlparse(absolute)

                    # Keep only same-domain absolute URLs
                    if parsed.netloc == base_domain:
                        links.add(absolute)

                browser.close()
        except Exception as e:
            self.logger.error(f"Error fetching links: {e}")

        self.links = list(links)
        return list(links)

    def fetch_content(self) -> str:
        """
        Extract all main text content from the webpage.

        Returns:
            str: Text paragraphs extracted from the page.
        """
        paragraphs = []
        self.logger.info(f"Fetching content from: {self.base_url}")

        try:
            with sync_playwright() as p:
                # Launch headless Chromium
                browser = p.chromium.launch(headless=True)
                page = browser.new_page()

                try:
                    # Go to the base URL and wait for network idle
                    page.goto(self.base_url, timeout=self.timeout)
                    page.wait_for_load_state("networkidle")
                except Exception as e:
                    self.logger.error(f"Timeout loading page: {self.base_url} | {e}")
                    return []

                # Get fully rendered HTML
                html = page.content()
                soup = BeautifulSoup(html, "html.parser")

                # Close the browser
                browser.close()

                for p_tag in soup.find_all("p"):
                    text = p_tag.get_text(strip=True)
                    if text:
                        paragraphs.append(text)
                    else:
                        self.logger.warning("Found empty paragraph tag, skipping.")
        except Exception as e:
            self.logger.error(f"Error fetching content: {e}")
        self.content = "\n\n".join(paragraphs)
        return self.content
