from fastapi import APIRouter, Depends, HTTPException
from medigo_server.schemas import ResponseModel, Category_Dto
from medigo_server.service import create_category_service, get_categories_service
from medigo_server.utils import get_current_user
from sqlalchemy.orm import Session
from medigo_server.database import get_db

#-------------------- integration of api's ---------------------
category_router = APIRouter(
    prefix="/category",
    tags=["categories"],
    responses={404: {"description": "Not found"}},
)

protected_router = APIRouter(
    dependencies=[Depends(get_current_user)]
)
public_router = APIRouter()

category_router.include_router(protected_router)
category_router.include_router(public_router)
#-------------------- integration of api's ---------------------

@protected_router.post("",response_model=ResponseModel)
async def create_category(request_model:Category_Dto,db:Session = Depends(get_db)) -> ResponseModel:
    try:
        return create_category_service(db,request_model)
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Error while adding category: {str(e)}"
        )

@public_router.get("",response_model=ResponseModel)
async def get_categories(db:Session = Depends(get_db)) -> ResponseModel:
    try:
        return get_categories_service(db)
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Error while getting categories: {str(e)}"
        )
