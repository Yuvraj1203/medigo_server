from fastapi import APIRouter, Depends, HTTPException, File, UploadFile
from medigo_server.schemas import ResponseModel, ProductDto
from medigo_server.utils import get_current_user
from medigo_server.database import get_db
from sqlalchemy.orm import Session
from medigo_server.service import add_product_service, get_products_service, delete_product_service

product_router = APIRouter(
    prefix="/products",
    tags=["products"],
    responses={404: {"description": "Not found"}},
)

@product_router.post("",response_model=ResponseModel,dependencies=[Depends(get_current_user)])
async def create_product(request_model:ProductDto, files: list[UploadFile] = File(...), db:Session = Depends(get_db)) -> ResponseModel:
    try:
        return await add_product_service(request_model, files, db)
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Error while adding product {e}"
        )

@product_router.get("",response_model=ResponseModel)
def get_products(db:Session = Depends(get_db)) -> ResponseModel:
    try:
        return get_products_service(db)
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Error while getting products: {str(e)}"
        )

@product_router.delete("/{id}",response_model=ResponseModel, dependencies=[Depends(get_current_user)])
def delete_product(id:str,db: Session = Depends(get_db)) -> ResponseModel:
    try: 
        return delete_product_service(db, id)
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Error while deleting product: {str(e)}"
        )
    