from app.core.repositories.interfaces.item_repository_interface import ItemRepositoryInterface
from app.core.services.interfaces.item_service_interface import ItemServiceInterface

class ItemServiceImpl(ItemServiceInterface):
    def __init__(self, item_repository: ItemRepositoryInterface) -> None:
        super().__init__(item_repository)