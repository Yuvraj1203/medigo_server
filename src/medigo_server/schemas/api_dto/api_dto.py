from pydantic import BaseModel
from typing import Optional, Any

class ResponseModel(BaseModel):
    success: Optional[bool] = True
    status: Optional[int] = 200
    result: Optional[Any] = None
    message: str
    unAuthorizedRequest: Optional[bool] = False