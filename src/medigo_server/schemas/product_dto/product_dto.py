from pydantic import BaseModel, Field, ConfigDict
from typing import Optional,List, Annotated
from medigo_server.common.enums import MedicineType
from uuid import UUID

class ProductDto(BaseModel):
    id: Annotated[UUID | None , Field(default=None)]
    name: str
    generic_name: Optional[str] = None
    brand: str
    category_id: str #foreign key
    requires_prescription: Optional[bool] = True
    description: Optional[str] = None
    manufacturer: Optional[str] = None
    medicine_type: MedicineType
    image_url: Optional[List[str]] = None
    is_active: Optional[bool] = True

    model_config = ConfigDict(from_attributes=True)  
