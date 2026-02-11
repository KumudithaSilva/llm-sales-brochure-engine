from typing import List
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup
from playwright.sync_api import Browser, sync_playwright

from interfaces.i_scraper import IScraperProvider


class PlaywrightWebScraper(IScraperProvider):
    """
    Playwright scraper.

    Responsibilities:
    - Handle dynamic JavaScript-rendered pages
    - Extract internal links
    - Extract main text content
    """

    def __init__(self, timeout: int = 10000, base_url=str):
        """
        Initialize scraper configuration.

        Args:
            Timeout in milliseconds
            Base URL for link extraction
        """
        self.timeout = timeout
        self.base_url = base_url
        self._playwright = None
        self._browser: Browser | None = None

    def fetch_links(self) -> List[str]:
        """
        Extract all valid internal links from a webpage.

        Returns:
            List[str]: A list of unique internal URLs found on the page.
        """
        with sync_playwright() as p:
            # Launch headless Chromium
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            # Go to the base URL and wait until network is idle
            page.goto(self.base_url, timeout=self.timeout)
            page.wait_for_load_state("networkidle")

            # Get fully rendered HTML
            html = page.content()
            soup = BeautifulSoup(html, "html.parser")

            base_domain = urlparse(self.base_url).netloc
            links = set()

            for tag in soup.find_all("a", href=True):
                href = tag["href"].strip()

                # Skip empty, mailto, tel, and anchor links
                if not href or href.startswith(("mailto:", "tel:", "#")):
                    continue

                # Convert relative to absolute
                absolute = urljoin(self.base_url, href)
                parsed = urlparse(absolute)

                # Keep only same-domain absolute URLs
                if parsed.netloc == base_domain:
                    links.add(absolute)

            browser.close()
            return list(links)

    def fetch_content(self) -> List[str]:
        """
        Extract all main text content from the webpage.

        Returns:
            List[str]: A list of text paragraphs extracted from the page.
        """
        with sync_playwright() as p:
            # Launch headless Chromium
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            # Go to the base URL and wait for network idle
            page.goto(self.base_url, timeout=self.timeout)
            page.wait_for_load_state("networkidle")

            # Get fully rendered HTML
            html = page.content()
            soup = BeautifulSoup(html, "html.parser")

            # Close the browser
            browser.close()

            paragraphs = []
            for p_tag in soup.find_all("p"):
                text = p_tag.get_text(strip=True)
                if text:
                    paragraphs.append(text)

            return paragraphs
