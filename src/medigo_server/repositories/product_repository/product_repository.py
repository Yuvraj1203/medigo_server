from sqlalchemy.orm import Session
from medigo_server.schemas import ProductDto, ResponseModel
from medigo_server.models import Product_Model
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
import logging
from medigo_server.core.decorators import handle_crud_exceptions

logger = logging.getLogger(__name__)

def add_product_crud(db:Session, data:ProductDto) -> ResponseModel:
    crud_name = "add_product_crud"
    try:
        existing_name = db.query(Product_Model).filter(Product_Model.name == data.name).first()

        existing = existing_name.brand == data.brand if existing_name else False

        if existing:
            raise ValueError("Product already exist")

        product = Product_Model(**data.model_dump())
        db.add(product)
        db.commit()
        db.refresh(product)
        return ResponseModel(result=ProductDto.model_validate(product))
    
    except ValueError as e:
        raise e
    
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


@handle_crud_exceptions
def get_products_crud(db:Session) -> ResponseModel:
    products = db.query(Product_Model).all()
    return ResponseModel(result=[ProductDto.model_validate(product) for product in products])

@handle_crud_exceptions
def delete_product_crud(db:Session, id:str) -> ResponseModel:
    product = db.query(Product_Model).filter(Product_Model.id == id).first()

    if not product:
        raise ValueError("Product not found")
    
    db.delete(product)
    db.commit()
    return ResponseModel(result=f"Product with id {id} deleted successfully")