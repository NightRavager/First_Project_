import pytest

from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.models.create_user_credit_request import CreateUserCreditRequest
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.credit_data import Credit
from src.main.api.models.user_credit_account_create import UserCreditAccountCreate
from src.main.api.models.create_credit_request import CreateCreditRequest
from src.main.api.models.create_account_credit_request import CreateAccountCreditRequest


@pytest.fixture
def user_credit_account_create(api_manager, create_user_credit_request):
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
def create_user_credit_request(api_manager):
    user_request = RandomModelGenerator.generate(CreateUserCreditRequest)
    api_manager.admin_steps.create_user(user_request)
    return user_request

@pytest.fixture
def create_account_credit_request(api_manager, create_user_credit_request: CreateUserCreditRequest):
    credit = RandomModelGenerator.generate(CreateAccountCreditRequest)
    account_credit = api_manager.user_credit_steps.create_credit(create_user_credit_request, credit)
    return account_credit