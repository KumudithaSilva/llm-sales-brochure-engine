import json
from typing import List

from openai import OpenAI

from interfaces.i_api_key_provider import IApiKeyProvider
from interfaces.i_oneshot_prompt import IPrompt
from interfaces.i_openai_operations import IOpenAIOperations
from logs.logger_singleton import Logger


class OpenAIService(IOpenAIOperations):
    """
    Service class for interacting with the OpenAI API.

    Attributes:
        key_provider (str): API key for OpenAI.
        system_prompt (str): System prompt for the AI.
        user_prompt (str): User prompt containing base URL and links.
        client (OpenAI): OpenAI client instance.
        model (str): Model name to use for completions.
        logger (Logger): Logger instance for info and error messages.
    """

    def __init__(
        self,
        key_provider: IApiKeyProvider,
        prompt_provider: IPrompt,
        base_url: str,
        links: list,
        logger=None,
    ):
        """
        Initialize OpenAIService with API key and prompts.

        Args:
            key_provider (IApiKeyProvider): Provider for OpenAI API key.
            prompt_provider (IPrompt): Provider for system and user prompts.
            base_url (str): Base URL for content context.
            links (list): List of links to process.
            logger (Logger, optional): Custom logger. Defaults to Logger singleton.
        """
        self.key_provider = key_provider.get_api_key()
        self.system_prompt = prompt_provider.system_prompt()
        self.user_prompt = prompt_provider.user_prompt(base_url, links)

        self.client = OpenAI(api_key=self.key_provider)
        self.model = "gpt-4"

        self.logger = logger or Logger(self.__class__.__name__)

    def select_relevant_links(self) -> List[str]:
        """
        Send prompts to OpenAI API and extract relevant links.

        Returns:
            List[str]: A list of relevant URLs extracted from AI response.
        """
        try:
            self.logger.info("Sending request to OpenAI API...")
            # Create chat completion request
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": self.user_prompt},
                ],
            )
            self.logger.info("Received response from OpenAI API.")

            # Extract the raw content from the first choice
            content = response.choices[0].message.content
            self.logger.debug(f"Raw response content: {content}")

            # Convert JSON response to Python dict and extract links
            data = json.loads(content)
            # Extracts only the URLs from the response
            links = [link["url"] for link in data.get("links", [])]

            self.logger.info(f"Extracted relevant links: {links}")
            return links

        except json.JSONDecodeError as e:
            # Handle invalid JSON returned from the AI
            self.logger.error(f"JSON decoding error: {e}")
            return []

        except Exception as e:
            # Handle any other unexpected errors
            self.logger.error(f"Error during OpenAI API call: {e}")
            return []
