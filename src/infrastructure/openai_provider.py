import os
from interfaces.i_api_key_provider import IApiKeyProvider
from interfaces.i_env_loader import IEnvLoader
from logs.logger_singleton import Logger

class OpenAIApiKeyProvider(IApiKeyProvider):
    def __init__(self, env_loader: IEnvLoader):
        """
        Initialize the DotEnvLoader class and configure the logger.
        """
        self.env_loader = env_loader
        self.logger = Logger(self.__class__.__name__)
    
    def get_api_key(self) -> str:
        """
        Load and validate the OpenAI API key from environment variables.

        Returns:
            str: The OpenAI API key if valid.

        Raises:
            EnvironmentError: If the API key is missing or invalid.
        """
        self.env_loader.load_env_variables()
        api_key = os.getenv('OPENAI_API_KEY')
         
        if not api_key:
            self.logger.error("Error: OPENAI_API_KEY not set")
            raise EnvironmentError("OPENAI_API_KEY not set")
         
        if api_key.startswith("sk-proj-"):
            self.logger.info("OpenAI API key found and validated")
            return api_key
        self.logger.error("Invalid OpenAI API key format")
        raise EnvironmentError("Invalid OpenAI API key format")