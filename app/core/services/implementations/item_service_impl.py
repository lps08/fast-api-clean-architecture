from app.core.repositories.interfaces.item_repository_interface import ItemRepositoryInterface
from app.core.services.interfaces.item_service_interface import ItemServiceInterface
from typing import List
from app.core.entities.item import Item

class ItemServiceImpl(ItemServiceInterface):
    def __init__(self, item_repository:ItemRepositoryInterface) -> None:
        self.item_repository = item_repository

    def create_item(self, name, description) -> Item:
        item = self.item_repository.create_item(name, description)
        
        return item

    def get_all(self) -> List[Item]:
        items = self.item_repository.get_all()

        return items
