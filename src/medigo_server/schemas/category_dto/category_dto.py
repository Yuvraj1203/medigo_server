from pydantic import BaseModel, Field, ConfigDict
from typing import Annotated, Optional
from uuid import UUID

class CategoryDto(BaseModel):
    id: Annotated[UUID | None, Field(default=None)]
    name: str
    description: str
    is_active: Annotated[bool,Field(default=True)]

    model_config = ConfigDict(from_attributes=True)  


class CategoryUpdateDto(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None

    model_config = ConfigDict(from_attributes=True)  