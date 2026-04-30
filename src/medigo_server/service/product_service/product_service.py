from medigo_server.schemas import ResponseModel, Product_Dto
from sqlalchemy.orm import Session
from medigo_server.repositories import add_product_crud

def add_product_service(data:Product_Dto,db:Session) -> ResponseModel:
    return add_product_crud(db,data)
