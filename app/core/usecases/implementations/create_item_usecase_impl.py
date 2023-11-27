from app.core.services.interfaces.item_service_interface import ItemServiceInterface
from app.core.usecases.interfaces.create_item_usecase_interface import CreateItemsUseCaseInterface

class CreateItemsUseCaseImpl(CreateItemsUseCaseInterface):
    def __init__(self, item_services: ItemServiceInterface) -> None:
        super().__init__(item_services)