from abc import ABC, abstractclassmethod
from typing import List
from core.entities.item import Item

class ItemRepositoryInterface(ABC):
    @abstractclassmethod
    def create_item(self, name, description) ->Item:
        pass

    @abstractclassmethod
    def get_all(self) -> List[Item]:
        pass