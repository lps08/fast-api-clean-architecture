from abc import ABC
from typing import List
from app.core.entities.item import Item
from app.core.services.interfaces.item_service_interface import ItemServiceInterface

class GetAllItemsUseCaseInterface(ABC):
    def __init__(self, item_services:ItemServiceInterface) -> None:
        self.item_services = item_services
    
    def execute(self) -> List[Item]:
        return self.item_services.get_all()