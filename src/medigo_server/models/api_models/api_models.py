from pydantic import BaseModel
from typing import Optional

class ResponseModel(BaseModel):
    success: Optional[bool] = True
    status: Optional[int] = 200
    message: str
    unAuthorizedRequest: Optional[bool] = False