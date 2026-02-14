import json
from typing import List

from openai import OpenAIError

from interfaces.i_ai_client import IAIClient
from interfaces.i_oneshot_prompt import IPrompt
from interfaces.i_openai_operations import IOpenAIOperations
from logs.logger_singleton import Logger


class OpenAIService(IOpenAIOperations):
    """
    Service class for interacting with an AI client.

    Attributes:
        ai_client (IAIClient): Abstract AI client.
        prompt_provider (IPrompt): Provides system and user prompts.
        client (OpenAI): OpenAI client instance.
        model (str): OpenAI model to use.
        logger (Logger): Logger instance for info and error messages.
    """

    def __init__(
        self,
        ai_client: IAIClient,
        prompt_provider: IPrompt,
        logger=None,
    ):
        """
        Initialize OpenAIService with AI client and prompt provider.

        Args:
            ai_client (IAIClient): Abstract AI client.
            prompt_provider (IPrompt): Provider for system and user prompts.
            logger (Logger, optional): Logger instance. Defaults to Logger singleton.
        """
        self.prompt_provider = prompt_provider

        self.system_prompt = self.prompt_provider.system_prompt()
        self.brochure_system_prompt = self.prompt_provider.brochure_system_prompt()

        self.user_prompt: str = ""
        self.brochure_user_prompt: str = ""

        self.ai_client = ai_client
        self.model = "gpt-4"

        self.logger = logger or Logger(self.__class__.__name__)

    def select_relevant_links(self, base_url: str, links: list) -> List[str]:
        """
        Send prompts to AI client and extract relevant links.

        Args:
            base_url (str): Website base URL.
            links (List[str]): List of URLs to filter.

        Returns:
            List[str]: Relevant links extracted from AI response.
        """
        self.user_prompt = self.prompt_provider.user_prompt(base_url, links)
        try:
            self.logger.info("Sending relevent links request to OpenAI API...")
            # Create chat completion request
            response = self.ai_client.chat_completions_create(
                system=self.system_prompt,
                user=self.user_prompt,
            )
            self.logger.info("Received response to relevant link from OpenAI API.")

            # Extract the raw content from the first choice
            content = response.choices[0].message.content
            self.logger.debug(f"Raw response content: {content}")

            # Convert JSON response to Python dict and extract links
            data = json.loads(content)
            # Extracts only the URLs from the response
            links = [link["url"] for link in data.get("links", [])]

            self.logger.info("Extracted relevant links")
            return links

        except json.JSONDecodeError as e:
            # Handle invalid JSON returned from the AI
            self.logger.error(f"JSON decoding error: {e}")
            return []

        except OpenAIError as oe:
            # Handle OpenAI API error
            self.logger.error(f"OpenAI API error: {oe}")
            return "Error: Failed to generate brochure due to API issue."

        except Exception as e:
            # Handle any other unexpected errors
            self.logger.error(f"Error during OpenAI API call: {e}")
            return []

    def create_brochure(
        self, company_name: str, contents: str, relevent_links: list
    ) -> str:
        """
        Generate a company brochure via AI client.

        Args:
            company_name (str): Name of the company.
            contents (str): Website contents.
            relevant_links (List[str]): Relevant URLs to include.

        Returns:
            str: Generated company brochure text.
        """
        self.brochure_user_prompt = self.prompt_provider.brochure_user_prompt(
            company_name, contents, relevent_links
        )
        try:
            self.logger.info("Sending brochure request to OpenAI API...")
            # Create chat completion request
            response = self.ai_client.chat_completions_create(
                system=self.brochure_system_prompt,
                user=self.brochure_user_prompt,
            )
            self.logger.info("Received brochure response from OpenAI API.")

            # Extract the raw content from the first choice
            content = response.choices[0].message.content
            self.logger.debug(f"Raw response content: {content}")

            return content

        except OpenAIError as oe:
            # OpenAI API error
            self.logger.error(f"OpenAI API error: {oe}")
            return "Error: Failed to generate brochure due to API issue."

        except Exception as e:
            # Handle any other unexpected errors
            self.logger.error(f"Unexpected error: {e}")
            return "Error: An unexpected error occurred while generating the brochure."
