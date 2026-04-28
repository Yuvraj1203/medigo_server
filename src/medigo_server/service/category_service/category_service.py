from medigo_server.schemas import Category_Dto, ResponseModel
from sqlalchemy.orm import Session
from medigo_server.repositories import create_category_crud
from fastapi import HTTPException

async def add_category(db:Session,category_model:Category_Dto) -> ResponseModel:
    try:
        return create_category_crud(db,category_model)
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Error while adding category: {str(e)}"
        )

