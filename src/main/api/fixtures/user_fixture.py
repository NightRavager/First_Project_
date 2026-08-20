from typing import Any

import pytest


from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.models.account_deposit_request_valid import AccountDepositRequestValid
from src.main.api.models.create_account_credit_request import CreateAccountCreditRequest
from src.main.api.models.create_user_credit_request import CreateUserCreditRequest
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.create_credit_request import CreateCreditRequest
from src.main.api.steps.user_steps import UserSteps
from src.main.api.models.account_create import AccountCreate


@pytest.fixture
def create_user_request(api_manager):
    user_request = RandomModelGenerator.generate(CreateUserRequest)
    api_manager.admin_steps.create_user(user_request)
    return user_request


@pytest.fixture
def create_user_id_request(api_manager):
    user_request = RandomModelGenerator.generate(CreateUserRequest)
    response = api_manager.admin_steps.create_user(user_request)
    return response

@pytest.fixture
def amount_account_deposit_request_valid(api_manager):
    amount = RandomModelGenerator.generate(AccountDepositRequestValid)
    return amount



@pytest.fixture
def account_deposit_request(account_create, amount = 1000):
    response = AccountDepositRequestValid(accountId=account_create.response.id, amount=amount)
    return response

@pytest.fixture
def account_user_request(api_manager, create_user_request: CreateUserRequest, create_account = UserSteps.create_account):
    credit_request = CreateCreditRequest(accountId= create_user_request.id)
    account_credit = api_manager.user_credit_steps.create_credit(create_user_request, credit_request)
    return account_credit

@pytest.fixture
def account_create(api_manager, create_user_request):
    response = api_manager.user_steps.create_account(create_user_request)
    return AccountCreate(
        response=response,
        create_user_request= create_user_request
    )

@pytest.fixture
def account_deposit_request_invalid_400(account_create, amount = -1000):
    response = AccountDepositRequestValid(accountId=account_create.response.id, amount=amount)
    return response

def create_account_request(api_manager, create_user_request: CreateUserRequest):
    credit = RandomModelGenerator.generate(CreateAccountCreditRequest)
    account_credit = api_manager.user_steps.create_credit(create_user_request, credit)
    return account_credit

@pytest.fixture
def account_create_with_balance(api_manager,
                                create_user_request,
                                account_deposit_request,
                                amount:float= 5000):
    account = api_manager.user_steps.create_account(create_user_request)
    deposit = AccountDepositRequestValid(accountId=account.id, amount=amount)
    response = api_manager.user_steps.account_deposit(create_user_request, deposit)

    return AccountCreateWithBalance(
        response=response,
        create_user_request= create_user_request
    )

