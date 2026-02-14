from typing import List, Optional

from interfaces.i_oneshot_prompt import IPrompt
from interfaces.i_openai_operations import IOpenAIOperations
from interfaces.i_sales_orchestrator import ISalesBrochureOrchestrator
from interfaces.i_scraper import IScraperProvider


class SalesBrochureOrchestrator(ISalesBrochureOrchestrator):
    """
    Orchestrates scraping and AI processing using interface-based dependencies.

    Attributes:
        playwright_scraper (IScraperProvider): Interface for web scraping.
        prompt_provider (IPrompt): Interface for prompt generation.
        openai_service (IOpenAIOperations): Interface for OpenAI operations.
        content (Optional[str]): Scraped content.
        base_url (Optional[str]): Base URL to scrape.
        links (Optional[List[str]]): All links fetched from the website.
    """

    def __init__(
        self,
        playwright_scraper: IScraperProvider,
        prompt_provider: IPrompt,
        openai_service: IOpenAIOperations,
    ):
        self.playwright_scraper = playwright_scraper
        self.prompt_provider = prompt_provider
        self.openai_service = openai_service

        self.content: Optional[str] = None
        self.base_url: Optional[str] = None
        self.links: Optional[List[str]] = None

    def orchestrate(self, base_url: str) -> str:
        """
        Fetch content and links from a website, select relevant links,
        and generate a company brochure.

        Args:
            base_url (str): The website URL.

        Returns:
            str: Generated company brochure.
        """
        self.base_url = base_url
        self.playwright_scraper.base_url = base_url

        # Fetch content and links
        self.content = self.playwright_scraper.fetch_content()
        self.links = self.playwright_scraper.fetch_links()

        # Select relevant links
        relevant_links = self.openai_service.select_relevant_links(base_url, self.links)
        links_text = "\n".join(relevant_links)

        # Generate company brochure
        brochure = self.openai_service.create_brochure(
            company_name="HuggingFace",
            contents=self.content,
            relevent_links=links_text,
        )

        return brochure
