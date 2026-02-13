from components.orchestrator import SalesBrochureOrchestrator
from infrastructure.dotenv import DotEnvLoader
from infrastructure.openai_client import OpenAIClientWrapper
from infrastructure.openai_provider import OpenAIApiKeyProvider
from infrastructure.openai_service import OpenAIService
from infrastructure.playwright_scraper import PlaywrightWebScraper
from infrastructure.prompt import PromptProvider
from interfaces.i_sales_orchestrator import ISalesBrochureOrchestrator


class SalesBrochureContainer:
    """Factory to wire all dependencies and return an orchestrator instance."""

    @staticmethod
    def create_orchestrator(base_url: str) -> ISalesBrochureOrchestrator:
        # Infrastructure
        env_loader = DotEnvLoader()
        key_provider = OpenAIApiKeyProvider(env_loader)
        ai_client = OpenAIClientWrapper(key_provider)

        # Scraper and prompt
        scraper = PlaywrightWebScraper(base_url=base_url)
        prompt_provider = PromptProvider()

        # OpenAI service
        openai_service = OpenAIService(ai_client, prompt_provider)

        # Orchestrator
        orchestrator: ISalesBrochureOrchestrator = SalesBrochureOrchestrator(
            playwright_scraper=scraper,
            prompt_provider=prompt_provider,
            openai_service=openai_service,
        )
        return orchestrator
