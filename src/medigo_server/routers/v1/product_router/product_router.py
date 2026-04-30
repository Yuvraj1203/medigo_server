from fastapi import APIRouter, Depends, HTTPException
from medigo_server.schemas import ResponseModel, Product_Dto
from medigo_server.utils import get_current_user
from medigo_server.database import get_db
from sqlalchemy.orm import Session
from medigo_server.service import add_product_service


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

@protected_router.post("/add-product",response_model=ResponseModel)
async def create_product_router(request_model:Product_Dto, db:Session = Depends(get_db)) -> ResponseModel:
    try:
        return add_product_service(request_model, db)
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Error while adding product {e}"
        )