from typing import Annotated

from src.main.api.models.base_model import BaseModel
from src.main.api.generators.creation_rule import CreationRule


class AccountDepositRequest(BaseModel):
    accountId: int
    amount: Annotated[float, CreationRule(regex=r'^[0-9]{1, 5}$')]