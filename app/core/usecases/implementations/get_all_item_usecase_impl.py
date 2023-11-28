from app.core.services.interfaces.item_service_interface import ItemServiceInterface
from app.core.usecases.interfaces.get_all_items_usecase_interface import GetAllItemsUseCaseInterface
from typing import List
from app.core.entities.item import Item

class GetAllItemsUseCaseImpl(GetAllItemsUseCaseInterface):
    def __init__(self, item_services:ItemServiceInterface) -> None:
        self.item_services = item_services
    
    def execute(self) -> List[Item]:
        return self.item_services.get_all()