from abc import ABC, abstractmethod
from typing import List
from core.entities.item import Item
from core.repositories.interfaces.item_repository_interface import ItemRepositoryInterface

class ItemServiceInterface(ABC):
    @abstractmethod
    def create_item(self, name, description) -> Item:
        pass

    @abstractmethod
    def get_all(self) -> List[Item]:
        pass