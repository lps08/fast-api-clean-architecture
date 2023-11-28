from abc import ABC, abstractmethod
from typing import List
from app.core.entities.item import Item
from app.core.services.interfaces.item_service_interface import ItemServiceInterface

class GetAllItemsUseCaseInterface(ABC):
    @abstractmethod
    def execute(self) -> List[Item]:
        pass