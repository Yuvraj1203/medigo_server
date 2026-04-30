from medigo_server.schemas import Category_Dto, ResponseModel
from sqlalchemy.orm import Session
from medigo_server.repositories import create_category_crud, get_categories_crud

def create_category_service(db:Session,category_model:Category_Dto) -> ResponseModel:
    return create_category_crud(db,category_model)

def get_categories_service(db:Session) -> ResponseModel:
    return get_categories_crud(db)

