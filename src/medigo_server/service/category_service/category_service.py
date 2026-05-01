from medigo_server.schemas import CategoryDto, ResponseModel, CategoryUpdateDto
from sqlalchemy.orm import Session
from medigo_server.repositories import create_category_crud, get_categories_crud, get_category_crud, update_category_crud, delete_category_crud

def create_category_service(db:Session,category_model:CategoryDto) -> ResponseModel:
    return create_category_crud(db,category_model)

def get_categories_service(db:Session) -> ResponseModel:
    return get_categories_crud(db)

def get_category_service(db:Session, id:str) -> ResponseModel:
    return get_category_crud(db, id)

def update_category_service(db:Session, id:str, request:CategoryUpdateDto) -> ResponseModel:
    return update_category_crud(db, id, request)

def delete_category_service(db:Session, id:str) -> ResponseModel:
    return delete_category_crud(db,id)