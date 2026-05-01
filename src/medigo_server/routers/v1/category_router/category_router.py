from fastapi import APIRouter, Depends, HTTPException
from medigo_server.schemas import ResponseModel, CategoryDto, CategoryUpdateDto
from medigo_server.service import create_category_service, get_categories_service, update_category_service, get_category_service, delete_category_service
from medigo_server.utils import get_current_user
from sqlalchemy.orm import Session
from medigo_server.database import get_db

#-------------------- integration of api's ---------------------
category_router = APIRouter(
    prefix="/category",
    tags=["categories"],
    responses={404: {"description": "Not found"}},
)
#-------------------- integration of api's ---------------------

@category_router.post("",response_model=ResponseModel, dependencies=[Depends(get_current_user)])
async def create_category(request_model:CategoryDto,db:Session = Depends(get_db)) -> ResponseModel:
    try:
        return create_category_service(db,request_model)
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Error while adding category: {str(e)}"
        )

@category_router.get("",response_model=ResponseModel)
async def get_categories(db:Session = Depends(get_db)) -> ResponseModel:
    try:
        return get_categories_service(db)
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Error while getting categories: {str(e)}"
        )

@category_router.get("/{id}",response_model=ResponseModel)
async def get_category(id:str, db:Session = Depends(get_db)) -> ResponseModel:
    try:
        return get_category_service(db, id)
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Error while getting category: {str(e)}"
        )

@category_router.patch("",response_model=ResponseModel, dependencies=[Depends(get_current_user)])
def update_category(id:str,request:CategoryUpdateDto,db:Session = Depends(get_db)) -> ResponseModel:
    try:
        return update_category_service(db,id,request)
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Error while updating category: {str(e)}"
        )
    
@category_router.delete("/{id}",response_model=ResponseModel, dependencies=[Depends(get_current_user)])
def delete_category(id:str, db:Session = Depends(get_db)) -> ResponseModel:
    try:
        return delete_category_service(db, id)
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Error while deleting category: {str(e)}"
        )