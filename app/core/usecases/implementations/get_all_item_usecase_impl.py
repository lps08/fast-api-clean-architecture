from app.core.services.interfaces.item_service_interface import ItemServiceInterface
from app.core.usecases.interfaces.get_all_items_usecase_interface import GetAllItemsUseCaseInterface

class GetAllItemsUseCaseImpl(GetAllItemsUseCaseInterface):
    def __init__(self, item_services: ItemServiceInterface) -> None:
        super().__init__(item_services)