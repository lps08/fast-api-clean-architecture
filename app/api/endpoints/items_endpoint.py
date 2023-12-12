from fastapi import APIRouter
from core.usecases.implementations.create_item_usecase_impl import CreateItemsUseCaseImpl

router = APIRouter()

create_item = CreateItemsUseCaseImpl()

@router.post("/item")
async def read_items(name:str, description:str):
    item = create_item.execute(name, description)
    return {
        'name' : item.name,
        'description' : item.description
    }