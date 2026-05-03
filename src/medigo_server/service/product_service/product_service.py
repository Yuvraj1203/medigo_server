from medigo_server.schemas import ResponseModel, ProductDto
from sqlalchemy.orm import Session
from medigo_server.repositories import add_product_crud, get_products_crud, delete_product_crud
from fastapi import UploadFile
import uuid
from medigo_server.database.file_bucket_db import supabase

async def add_product_service(data:ProductDto, files:list[UploadFile], db:Session) -> ResponseModel:
    # add image to bucket
    urls: list[str] = []

    for file in files:
        if not file.filename:
            raise ValueError("Invalid file")
        
        file_ext = (file.filename).split(".")[-1]
        file_name = f"{uuid.uuid4()}.{file_ext}"

        file_bytes = await file.read()

        #upload to bucket
        supabase.storage.from_("product-images").upload(
            path=file_name,
            file=file_bytes,
            file_options={"content-type": file.content_type or "application/octet-stream"}
        )

        public_url = supabase.storage.from_("product-images").get_public_url(file_name)

        urls.append(public_url)

    # attach URLs to product
    data.image_url = urls
    # add json to db
    return add_product_crud(db,data)

def get_products_service(db:Session) -> ResponseModel:
    return get_products_crud(db)

def delete_product_service(db:Session, id:str) -> ResponseModel:
    return delete_product_crud(db, id)