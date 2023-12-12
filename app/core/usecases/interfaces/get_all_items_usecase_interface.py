from abc import ABC, abstractmethod
from typing import List
from core.entities.item import Item
from core.services.interfaces.item_service_interface import ItemServiceInterface

class GetAllItemsUseCaseInterface(ABC):
    @abstractmethod
    def execute(self) -> List[Item]:
        pass