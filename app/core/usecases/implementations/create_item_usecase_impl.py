from app.core.services.interfaces.item_service_interface import ItemServiceInterface
from app.core.usecases.interfaces.create_item_usecase_interface import CreateItemsUseCaseInterface
from app.core.entities.item import Item

class CreateItemsUseCaseImpl(CreateItemsUseCaseInterface):
    def __init__(self, item_services:ItemServiceInterface) -> None:
        self.item_services = item_services
    
    def execute(self, name, description) -> Item:
        return self.item_services.create_item(name, description)
