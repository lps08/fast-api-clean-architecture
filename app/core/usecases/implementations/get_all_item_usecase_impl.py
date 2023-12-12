from core.services.interfaces.item_service_interface import ItemServiceInterface
from core.services.implementations.item_service_impl import ItemServiceImpl
from core.usecases.interfaces.get_all_items_usecase_interface import GetAllItemsUseCaseInterface
from typing import List
from core.entities.item import Item

class GetAllItemsUseCaseImpl(GetAllItemsUseCaseInterface):
    def __init__(self, item_services:ItemServiceInterface = ItemServiceImpl()) -> None:
        self.item_services = item_services
    
    def execute(self) -> List[Item]:
        return self.item_services.get_all()