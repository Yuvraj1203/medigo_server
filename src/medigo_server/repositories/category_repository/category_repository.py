from medigo_server.models import Category_Model
from medigo_server.schemas import CategoryDto, ResponseModel, CategoryUpdateDto
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
import logging 
from medigo_server.core.decorators import handle_crud_exceptions
from uuid import UUID

logger = logging.getLogger(__name__) #to log with the file name

def create_category_crud(db:Session,data:CategoryDto) -> ResponseModel:
    crud_name = "create_category_crud"
    try:
        existing = db.query(Category_Model).filter(Category_Model.name == data.name).first()

        if existing:
            raise ValueError("Category already exist")

        category = Category_Model(**data.model_dump())
        db.add(category)
        db.commit()
        db.refresh(category)
        return ResponseModel(result=CategoryDto.model_validate(category))
    
    except ValueError as e:
        raise e
    
    except IntegrityError as e:
        db.rollback()
        logger.error(f"IntegrityError on {crud_name}: {e}")
        raise ValueError(f"Duplicate or constraint error")
    
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"SQL Error on {crud_name}: {e}")
        raise RuntimeError(f"Database error occurred")
    
    except Exception as e:
        db.rollback()
        logger.error(f"Unexpected error on {crud_name}: {e}")
        raise RuntimeError("Something went wrong")
    
@handle_crud_exceptions
def get_categories_crud(db:Session) -> ResponseModel:
    categories = db.query(Category_Model).all()
    return ResponseModel(result=[CategoryDto.model_validate(category) for category in categories])

@handle_crud_exceptions
def get_category_crud(db: Session, id:str) -> ResponseModel:
    category = db.query(Category_Model).filter(Category_Model.id == UUID(id)).first()

    if not category:
        raise ValueError("Category not found")
    
    return ResponseModel(result=CategoryDto.model_validate(category))

@handle_crud_exceptions
def update_category_crud(db:Session, id:str, request:CategoryUpdateDto) -> ResponseModel:
    category = db.query(Category_Model).filter(Category_Model.id == UUID(id)).first()

    if not category:
        raise ValueError("Category not found")
    
    data = request.model_dump(exclude_unset=True)
    
    if not data:
        raise ValueError("No fields provided for update")

    for key, value in data.items():
        setattr(category, key, value)

    db.commit()
    db.refresh(category)
    return ResponseModel(result=CategoryUpdateDto.model_validate(category))

@handle_crud_exceptions
def delete_category_crud(db:Session, id: str) -> ResponseModel:
    category = db.query(Category_Model).filter(Category_Model.id == UUID(id)).first()

    if not category:
        raise ValueError("Category not found")
    
    db.delete(category)
    db.commit()
    return ResponseModel(result=f"Category with id {id} deleted successfully")