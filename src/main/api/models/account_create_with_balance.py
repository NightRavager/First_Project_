from src.main.api.models.account_deposit_response import AccountDepositResponse
from src.main.api.models.base_model import BaseModel
from src.main.api.models.create_account_response import CreateAccountResponse
from src.main.api.models.create_user_request import CreateUserRequest


class AccountCreateWithBalance(BaseModel):
        response: AccountDepositResponse
        create_user_request: CreateUserRequest
