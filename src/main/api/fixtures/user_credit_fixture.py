import pytest
from api.utils.constants import CreditData
from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.models.create_user_credit_request import CreateUserCreditRequest
from src.main.api.models.user_credit_account_create import UserCreditAccountCreate
from src.main.api.models.create_credit_request import CreateCreditRequest



@pytest.fixture
def user_credit_account_create(api_manager, create_user_credit_request: CreateUserCreditRequest):
    response = api_manager.user_steps.create_account(create_user_credit_request)
    return UserCreditAccountCreate(
        response=response,
        create_user_credit_request= create_user_credit_request
    )

@pytest.fixture
def create_user_credit_request(api_manager):
    user_credit_request = RandomModelGenerator.generate(CreateUserCreditRequest)
    api_manager.admin_steps.create_user_credit(user_credit_request)
    return user_credit_request

@pytest.fixture
def create_account_credit_request(api_manager, user_credit_account_create: UserCreditAccountCreate):
        create_credit_request = CreateCreditRequest(accountId=user_credit_account_create.response.id,
                                                    amount=CreditData.DEFAULT_AMOUNT_BALANCE,
                                                    termMonths=CreditData.DEFAULT_TERM_MONTHS)
        response = api_manager.user_credit_steps.create_credit(user_credit_account_create.create_user_credit_request,
                                                    create_credit_request)
        return response

