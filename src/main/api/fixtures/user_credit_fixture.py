import pytest

from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.models.create_user_credit_request import CreateUserCreditRequest
from src.main.api.models.create_user_request import CreateUserRequest


@pytest.fixture
def create_user_credit_request(api_manager):
    user_credit_request = RandomModelGenerator.generate(CreateUserCreditRequest)
    api_manager.admin_steps.create_user_credit(user_credit_request)
    return user_credit_request