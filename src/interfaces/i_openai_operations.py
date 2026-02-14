from abc import ABC, abstractmethod
from typing import List


class IOpenAIOperations(ABC):

    @abstractmethod
    def select_relevant_links(self, base_url: str, links: list) -> List[str]:
        pass

    @abstractmethod
    def create_brochure(
        self, company_name: str, contents: str, relevent_links: list
    ) -> str:
        pass
