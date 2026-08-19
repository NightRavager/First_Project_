import pytest

from src.main.api.models.account_deposit_request import AccountDepositRequest
from src.main.api.models.account_transfer_request import AccountTransferRequest


@pytest.mark.api
class TestAccountDeposit:
    def test_account_deposit(self, api_manager, create_user_request):
        create_account_credit = api_manager.user_steps.create_account(create_user_request)
        amount = 1000
        account_deposit_request = AccountDepositRequest(accountId=create_account_credit.id, amount=amount)
        response = api_manager.user_steps.account_deposit(create_user_request, account_deposit_request)

        assert create_account_credit.balance == response.balance - account_deposit_request.amount


    def test_account_deposit_invalid_400(self, api_manager, create_user_request):
        create_account_credit = api_manager.user_steps.create_account(create_user_request)
        amount = -1000
        account_deposit_request = AccountDepositRequest(accountId=create_account_credit.id, amount=amount)
        api_manager.user_steps.account_deposit_invalid_400(create_user_request, account_deposit_request)



