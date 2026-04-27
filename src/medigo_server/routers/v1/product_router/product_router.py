from fastapi import APIRouter, Depends
from medigo_server.schemas import ResponseModel, Product_Dto
from medigo_server.utils import get_current_user

product_router = APIRouter(
    prefix="/products",
    tags=["products"],
    responses={404: {"description": "Not found"}},
)

protected_router = APIRouter(
    dependencies=[Depends(get_current_user)]
)
public_router = APIRouter()

product_router.include_router(protected_router)
product_router.include_router(public_router)

@product_router.post("/add-product",response_model=ResponseModel)
async def create_product_router(request_model:Product_Dto) -> None:
    pass