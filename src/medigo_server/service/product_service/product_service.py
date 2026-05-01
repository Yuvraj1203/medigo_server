from medigo_server.schemas import ResponseModel, ProductDto
from sqlalchemy.orm import Session
from medigo_server.repositories import add_product_crud, get_products_crud, delete_product_crud

def add_product_service(data:ProductDto,db:Session) -> ResponseModel:
    return add_product_crud(db,data)

def get_products_service(db:Session) -> ResponseModel:
    return get_products_crud(db)

def delete_product_service(db:Session, id:str) -> ResponseModel:
    return delete_product_crud(db, id)