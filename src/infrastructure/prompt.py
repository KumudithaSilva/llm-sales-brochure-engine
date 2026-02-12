from logging import Logger
from typing import List

from interfaces.i_oneshot_prompt import IPrompt


class PromptProvider(IPrompt):
    """
    Provider system and user prompts for one-shot learning tasks.
    """

    def __init__(self, logger=None):
        """
        Initialize the PromptProvider instance.

        Args:
            logger (Logger, optional): A logger instance. If None, a
                default logger is created using the class name.
        """
        self.logger = logger or Logger(self.__class__.__name__)

    def system_prompt(self) -> str:
        """
        Get the system prompt.

        Returns:
            str: The system prompt string.
        """
        system_prompt = """
        You are provided with a list of links found on a webpage.
        You are able to decide which of the links would be most relevant to include in a brochure about the company,
        such as links to an About page, or a Company page, or Careers/Jobs pages.
        You should respond in JSON as in this example:

        {
            "links": [
                {"type": "about page", "url": "https://full.url/goes/here/about"},
                {"type": "careers page", "url": "https://another.full.url/careers"}
            ]
        } 
        """
        return system_prompt

    def user_prompt(self, base_url: str, links: List[str]) -> str:
        """
        Get the user prompt.

        Returns:
            str: The user prompt string.
        """
        user_prompt = f"""
        Here is the list of links on the website {base_url} -
        Please decide which of these are relevant web links for a brochure about the company, 
        respond with the full https URL in JSON format.
        Do not include Terms of Service, Privacy, email links.

        Links (some might be relative links): {links}

        """
        return user_prompt
