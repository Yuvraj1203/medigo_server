from pydantic import BaseModel, Field
from typing import Annotated

print("hi")
class CategoryDto(BaseModel):
    id: Annotated[str | None, Field(default=None)]
    name: str
    description: str
    is_active: Annotated[bool,Field(default=True)]

category = CategoryDto(id="bhdskjbhfdsjbfjhsb",name="Painkillers", description="Medications used to relieve pain", is_active=True)

print("category=>",category)
print("CategoryDto.model_validate==>",CategoryDto.model_validate(category))

print("CategoryDto.model_dump==>",CategoryDto.model_dump(category))