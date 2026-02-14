from abc import ABC, abstractmethod


class IAIClient(ABC):
    """
    Abstract interface for an AI client.
    """

    @abstractmethod
    def chat_completions_create(self, system: str, user: str) -> str:
        """
        Sends a chat completion request to the AI backend.

        Args:
            system (str): System prompt.
            user (str): User prompt.

        Returns:
            str: AI response content.
        """
        pass
