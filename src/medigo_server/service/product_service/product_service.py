from medigo_server.schemas import ResponseModel, Product_Dto
from sqlalchemy.orm import Session
from medigo_server.repositories import add_product_crud, get_products_crud

def add_product_service(data:Product_Dto,db:Session) -> ResponseModel:
    return add_product_crud(db,data)

def get_products_service(db:Session) -> ResponseModel:
    return get_products_crud(db)