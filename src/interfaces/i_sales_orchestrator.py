from abc import ABC, abstractmethod


class ISalesBrochureOrchestrator(ABC):
    """
    Interface for orchestrating website scraping and AI processing.
    """

    @abstractmethod
    def orchestrate(self, base_url: str) -> str:
        """
        Fetch content and links from the website, select relevant links,
        and generate a company brochure.

        Args:
            base_url (str): The website URL.

        Returns:
            str: Generated company brochure.
        """
        pass
