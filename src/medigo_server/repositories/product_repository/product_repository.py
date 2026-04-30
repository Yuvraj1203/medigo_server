from sqlalchemy.orm import Session
from medigo_server.schemas import Product_Dto, ResponseModel
from medigo_server.models import Product_Model
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
import logging

logger = logging.getLogger(__name__)

def add_product_crud(db:Session, data:Product_Dto) -> ResponseModel:
    crud_name = "add_product_crud"
    try:
        existing = db.query(Product_Model).filter(Product_Model.name == data.name).first()

        if existing:
            raise ValueError("Product already exist")

        product = Product_Model(**data.model_dump())
        db.add(product)
        db.commit()
        db.refresh(product)
        return ResponseModel(result=product)
    
    except IntegrityError as e:
        db.rollback()
        logger.error(f"IntegrityError on {crud_name}: {e}")
        raise ValueError("Duplicate or constraint error on add_product_crud")
    
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"SQL Error on {crud_name}: {e}")
        raise RuntimeError("Database error occurred on add_product_crud")

    except Exception as e:
        db.rollback()
        logger.error(f"Unexpected error on {crud_name}: {e}")
        raise RuntimeError("Something went wrong")
