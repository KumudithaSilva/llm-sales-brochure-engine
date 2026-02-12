from abc import ABC, abstractmethod
from typing import List


class IOpenAIOperations(ABC):

    @abstractmethod
    def select_relevant_links(self) -> List[str]:
        pass
