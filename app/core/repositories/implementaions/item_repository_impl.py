from app.core.repositories.interfaces.item_repository_interface import ItemRepositoryInterface
from app.core.entities.item import Item
from typing import List

class ItemRepositoryImpl(ItemRepositoryInterface):
    def __init__(self) -> None:
        self.list = []

    def create_item(self, name, description) ->Item:
        item = Item(name, description)
        self.list.append(item)

        return item
    
    def get_all(self) -> List[Item]:
        return self.list