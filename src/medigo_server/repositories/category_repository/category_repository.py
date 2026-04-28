from medigo_server.models import Category_Model
from medigo_server.schemas import Category_Dto, ResponseModel
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

def create_category_crud(db:Session,data:Category_Dto) -> ResponseModel:
    try:
        existing = db.query(Category_Model).filter(Category_Model.name == data.name).first()

        if existing:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Category already exists"
            )

        category = Category_Model(**data.model_dump())
        db.add(category)
        db.commit()
        db.refresh(category)
        return ResponseModel(result=Category_Dto.model_validate(category))
    except Exception as e:
        db.rollback()
        print("ERROR:", e)
        raise e