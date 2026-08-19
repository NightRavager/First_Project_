from typing import List, Dict

from pydantic import RootModel

from src.main.api.models.base_model import BaseModel



class UserResponse(BaseModel):
    id: int
    username: str
    role: str

class AdminUsersResponse(RootModel[list[UserResponse]]):
    pass

