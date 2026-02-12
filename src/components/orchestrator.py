from typing import List, Optional

from infrastructure.dotenv import DotEnvLoader
from infrastructure.openai_provider import OpenAIApiKeyProvider
from infrastructure.openai_service import OpenAIService
from infrastructure.playwright_scraper import PlaywrightWebScraper
from infrastructure.prompt import PromptProvider


class SalesBrochureOrchestrator:
    """
    Orchestrates the process of scraping website links and filtering
    them using OpenAI's API for relevance.

    Attributes:
        env_loader (DotEnvLoader): Loads environment variables.
        key_provider (OpenAIApiKeyProvider): Provides OpenAI API key.
        playwright_scraper (Optional[PlaywrightWebScraper]): Scraper instance.
        prompt_provider (Optional[PromptProvider]): Provides prompts for OpenAI.
        base_url (Optional[str]): The base URL to scrape.
        links (list): All links fetched from the base URL.
    """

    def __init__(self):
        """Initialize the orchestrator with environment loader and API key provider."""
        self.env_loader = DotEnvLoader()
        self.key_provider = OpenAIApiKeyProvider(self.env_loader)

        self.playwright_scraper: Optional[PlaywrightWebScraper] = None
        self.prompt_provider: Optional[PromptProvider] = None

        self.base_url: Optional[str] = None
        self.links: list = []

    def orchestrate(self, base_url: str) -> List[str]:
        """
        Main orchestration method: fetch links from the website and
        select relevant links via OpenAI.

        Steps:
            1. Initialize the Playwright scraper with the base URL.
            2. Fetch all internal links from the website.
            3. Initialize PromptProvider if not already created.
            4. Call OpenAIService to select relevant links.

        Args:
            base_url (str): The website URL.

        Returns:
            List[str]: A list of relevant links identified by OpenAI.
        """
        self.base_url = base_url
        self.playwright_scraper = PlaywrightWebScraper(base_url=self.base_url)
        self.links = self.playwright_scraper.fetch_links()

        if self.prompt_provider is None:
            self.prompt_provider = PromptProvider()
        openai_service = OpenAIService(
            self.key_provider, self.prompt_provider, self.base_url, self.links
        )
        relevant_links = openai_service.select_relevant_links()
        return relevant_links
