from core.repositories.implementaions.item_repository_impl import ItemRepositoryImpl
from core.repositories.interfaces.item_repository_interface import ItemRepositoryInterface
from core.services.implementations.item_service_impl import ItemServiceImpl
from fastapi import Depends

def get_item_repository() -> ItemRepositoryImpl:
    item_repository = ItemRepositoryImpl()
    return item_repository

def get_item_service(item_repository:ItemRepositoryInterface = Depends(get_item_repository)) -> ItemServiceImpl:
    item_service = ItemServiceImpl(item_repository)
    return item_service