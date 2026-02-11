from abc import ABC, abstractmethod
from typing import List, Tuple


class IScraperProvider(ABC):

    @abstractmethod
    def fetch_links(self) -> List[str]:
        """Return a list of valid web links from the base URL."""
        pass

    @abstractmethod
    def fetch_content(self) -> Tuple[str, str]:
        """Return the page title and main content."""
        pass
