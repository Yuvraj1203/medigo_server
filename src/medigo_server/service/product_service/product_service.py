from medigo_server.schemas import ResponseModel, Product_Dto
from sqlalchemy.orm import Session
from fastapi import HTTPException
from medigo_server.repositories import add_product_crud

def add_product_service(data:Product_Dto,db:Session) -> ResponseModel:
    try:
        return add_product_crud(db,data)
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Error while adding product {e}"
        )
