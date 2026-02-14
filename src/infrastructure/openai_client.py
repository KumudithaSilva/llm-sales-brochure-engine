from openai import OpenAI

from interfaces.i_ai_client import IAIClient
from interfaces.i_api_key_provider import IApiKeyProvider


class OpenAIClientWrapper(IAIClient):
    """
    Concrete wrapper for the OpenAI Python library.

    Attributes:
        key_provider (str): API key obtained from IApiKeyProvider.
        client (OpenAI): OpenAI client instance.
        model (str): Model name to use for chat completions.
    """

    def __init__(self, key_provider: IApiKeyProvider, model: str = "gpt-4"):
        """
        Initialize OpenAI client wrapper.

        Args:
            key_provider (IApiKeyProvider): Interface to obtain OpenAI API key.
            model (str, optional): Name of the OpenAI model.
        """
        self.key_provider = key_provider.get_api_key()
        self.client = OpenAI(api_key=self.key_provider)
        self.model = model

    def chat_completions_create(self, system: str, user: str) -> str:
        """
        Calls OpenAI chat completion API.

        Args:
            system (str): System prompt.
            user (str): User prompt.

        Returns:
            str: Content of the AI response.
        """
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
        )
        return response
