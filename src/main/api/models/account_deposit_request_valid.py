from typing import Annotated

from src.main.api.models.base_model import BaseModel
from src.main.api.generators.creation_rule import CreationRule


class AccountDepositRequestValid(BaseModel):
    accountId: int
    amount: float #Annotated[float, CreationRule(regex= None, min_value=1000, max_value=9000)]