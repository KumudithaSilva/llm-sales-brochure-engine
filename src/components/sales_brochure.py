from infrastructure.dotenv import DotEnvLoader
from infrastructure.openai_provider import OpenAIApiKeyProvider

class SalesBrochure:
    
    def __init__(self):
        self.env_loader = DotEnvLoader()
        self.api_key_provider = OpenAIApiKeyProvider(self.env_loader)


if __name__ == "__main__":
    sales_brochure = SalesBrochure()
    print(sales_brochure.api_key_provider.get_api_key())