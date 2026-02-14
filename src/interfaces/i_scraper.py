from abc import ABC, abstractmethod
from typing import List


class IScraperProvider(ABC):

    @abstractmethod
    def fetch_links(self) -> List[str]:
        """Return a list of valid web links from the base URL."""
        pass

    @abstractmethod
    def fetch_content(self) -> str:
        """Return the page title and main content."""
        pass
