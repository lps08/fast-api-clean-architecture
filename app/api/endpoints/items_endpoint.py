from fastapi import APIRouter
from core.services.interfaces.item_service_interface import ItemServiceInterface
from core.usecases.implementations.create_item_usecase_impl import CreateItemsUseCaseImpl
from core.usecases.implementations.get_all_item_usecase_impl import GetAllItemsUseCaseImpl
from fastapi import Depends
from api.dependencies import dependencies

router = APIRouter()

@router.post("/item")
async def create_item(name:str, description:str, service:ItemServiceInterface = Depends(dependencies.get_item_service)):
    create_item_usecase = CreateItemsUseCaseImpl(service)
    item = create_item_usecase.execute(name, description)
    return {
        "name" : item.name,
        "description" : item.description
    }

@router.get("/items")
async def read_items(service:ItemServiceInterface = Depends(dependencies.get_item_service)):
    get_all_usecase = GetAllItemsUseCaseImpl(service)
    items = get_all_usecase.execute()
    return {
        'items' : [{"name":item.name, "description":item.description} for item in items]
    }