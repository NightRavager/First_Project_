from src.main.api.models.base_model import BaseModel
from src.main.api.models.create_account_response import CreateAccountResponse
from src.main.api.models.create_creadit_response import CreateCreditResponse
from src.main.api.models.create_user_credit_request import CreateUserCreditRequest
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.user_credit_account_create import UserCreditAccountCreate
from src.main.api.models.create_credit_request import CreateCreditRequest


class Credit(BaseModel):
        user_credit_account_create: UserCreditAccountCreate
        create_credit_request: CreateCreditRequest
        create_credit_response: CreateCreditResponse
