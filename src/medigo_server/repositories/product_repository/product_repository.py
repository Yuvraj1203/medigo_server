from sqlalchemy.orm import Session
from medigo_server.schemas import Product_Dto, ResponseModel
from medigo_server.models import Product_Model
from fastapi import HTTPException, status

def add_product_crud(db:Session, data:Product_Dto) -> ResponseModel:
    try:
        existing = db.query(Product_Model).filter(Product_Model.name == data.name).first()

        if existing:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Product already exist"
            )

        product = Product_Model(**data.model_dump())
        db.add(product)
        db.commit()
        db.refresh(product)
        return ResponseModel(result=product)
    except Exception as e:
        db.rollback()
        raise e
