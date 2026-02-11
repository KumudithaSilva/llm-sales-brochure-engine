from infrastructure.dotenv import DotEnvLoader
from infrastructure.openai_provider import OpenAIApiKeyProvider
from infrastructure.playwright_scraper import PlaywrightWebScraper


class SalesBrochure:

    def __init__(self):
        self.env_loader = DotEnvLoader()
        self.api_key_provider = OpenAIApiKeyProvider(self.env_loader)
        self.pywright_scraper = PlaywrightWebScraper(
            base_url="https://www.example.com/sales-brochure"
        )


if __name__ == "__main__":
    sales_brochure = SalesBrochure()
