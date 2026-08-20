import pytest


from src.main.api.models.account_deposit_request_valid import AccountDepositRequestValid
from src.main.api.models.account_transfer_request import AccountTransferRequest
from src.main.api.models.create_account_credit_request import CreateAccountCreditRequest
from src.main.api.models.create_user_request import CreateUserRequest


@pytest.mark.api
class TestAccountDeposit:
    def test_account_deposit(self, api_manager, account_create, account_deposit_request):

        response = api_manager.user_steps.account_deposit(account_create.create_user_request,account_deposit_request)

        assert response.balance == account_deposit_request.amount


    def test_account_deposit_invalid_404(self, api_manager, account_create, account_deposit_request):
        account_deposit_request.accountId += 1
        api_manager.user_steps.account_deposit_invalid_404(account_create.create_user_request,account_deposit_request)
