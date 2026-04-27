from pydantic import BaseModel
from typing import Optional,List
from medigo_server.common.enums import MedicineType

class Product_Dto(BaseModel):
    id: str
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
