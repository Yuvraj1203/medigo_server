from medigo_server.models import Category_Model
from medigo_server.schemas import Category_Dto, ResponseModel
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
import logging 
from medigo_server.core.decorators import handle_crud_exceptions

logger = logging.getLogger(__name__) #to log with the file name

def create_category_crud(db:Session,data:Category_Dto) -> ResponseModel:
    crud_name = "create_category_crud"
    try:
        existing = db.query(Category_Model).filter(Category_Model.name == data.name).first()

        if existing:
            raise ValueError("Category already exist")

        category = Category_Model(**data.model_dump())
        db.add(category)
        db.commit()
        db.refresh(category)
        return ResponseModel(result=Category_Dto.model_validate(category))
    
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
    categories = db.query(Category_Dto).all()
    return ResponseModel(result=categories)