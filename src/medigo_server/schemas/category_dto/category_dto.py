from pydantic import BaseModel, Field
from typing import Annotated

class Category_Dto(BaseModel):
    id: Annotated[str | None, Field(default=None)]
    name: str
    description: str
    is_active: Annotated[bool,Field(default=True)]