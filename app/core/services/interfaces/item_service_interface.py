from abc import ABC, abstractmethod
from typing import List
from app.core.entities.item import Item
from app.core.repositories.interfaces.item_repository_interface import ItemRepositoryInterface

class ItemServiceInterface(ABC):
    @abstractmethod
    def create_item(self, name, description) -> Item:
        pass

    @abstractmethod
    def get_all(self) -> List[Item]:
        pass