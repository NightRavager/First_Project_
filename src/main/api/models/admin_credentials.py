from src.main.api.models.base_model import BaseModel


class AdminCredentials(BaseModel):
    username: str
    password: str