from infrastructure.dotenv import DotEnvLoader
from infrastructure.openai_provider import OpenAIApiKeyProvider
from infrastructure.playwright_scraper import PlaywrightWebScraper
from typing import List


class SalesBrochure:

    def __init__(self):
        self.env_loader = DotEnvLoader()
        self.api_key_provider = OpenAIApiKeyProvider(self.env_loader)
        self.pywright_scraper = None
    
    def fetch_links(self, base_url: str) -> List[str]:
        self.pywright_scraper = PlaywrightWebScraper(base_url=base_url)
        links = self.pywright_scraper.fetch_links()
        return links