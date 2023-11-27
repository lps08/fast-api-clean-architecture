from abc import ABC, abstractclassmethod
from typing import List
from app.core.entities.item import Item
from app.core.repositories.interfaces.item_repository_interface import ItemRepositoryInterface

class ItemServiceInterface(ABC):
    def __init__(self, item_repository:ItemRepositoryInterface) -> None:
        self.item_repository = item_repository

    def create_item(self, name, description) -> Item:
        item = self.item_repository.create_item(name, description)
        
        return item

    def get_all(self) -> List[Item]:
        items = self.item_repository.get_all()

        return items
