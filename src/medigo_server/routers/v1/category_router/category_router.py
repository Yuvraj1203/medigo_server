from fastapi import APIRouter, Depends
from medigo_server.schemas import ResponseModel, Category_Dto
from medigo_server.service import add_category
from medigo_server.utils import get_current_user

#-------------------- integration of api's ---------------------
category_router = APIRouter(
    prefix="/category",
    tags=["categories"],
    responses={404: {"description": "Not found"}},
)

protected_router = APIRouter(
    dependencies=[Depends(get_current_user)]
)
public_router = APIRouter()

category_router.include_router(protected_router)
category_router.include_router(public_router)
#-------------------- integration of api's ---------------------

@category_router.post("/add-category",response_model=ResponseModel)
async def create_product_category_router(request_model:Category_Dto) -> ResponseModel:
    return await add_category(request_model)
