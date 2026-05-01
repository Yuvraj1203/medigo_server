from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from functools import wraps
from sqlalchemy.orm import Session
import logging
from typing import Callable, TypeVar, Any, cast

T = TypeVar("T")  # return type of wrapped function

def handle_crud_exceptions(func: Callable[..., T]) -> Callable[..., T]:
    logger = logging.getLogger(func.__module__)  

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> T:
        db:Session = kwargs.get('db') or args[0]

        try:
            return func(*args,**kwargs)
        
        except ValueError as e:  
            raise e
        
        except IntegrityError as e:
            db.rollback()
            logger.error(f"{func.__name__} IntegrityError: {e}")
            raise ValueError("Duplicate or constraint error")
        
        except SQLAlchemyError as e:
            db.rollback()
            logger.error(f"{func.__name__} SQLAlchemyError: {e}")
            raise RuntimeError("Database error occurred")
        
        except Exception as e:
            db.rollback()
            logger.error(f"{func.__name__} Unexpected error: {e}")
            raise RuntimeError("Something went wrong")
        
    return cast(Callable[..., T], wrapper)
        