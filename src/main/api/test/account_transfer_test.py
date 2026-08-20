import pytest

from src.main.api.configs.config import Config
from src.main.api.models.account_deposit_request_valid import AccountDepositRequestValid
from src.main.api.models.account_transfer_request import AccountTransferRequest


@pytest.mark.api
class TestTransfer:
    def test_account_transfer(self, api_manager, create_user_request,
                              amount_account_deposit_request_valid,
                              account_create_with_balance,
                              account_create):
        account_transfer_request = AccountTransferRequest(fromAccountId=account_create_with_balance.id,
                                                          toAccountId=account_create.id,
                                                          amount=1000)

        response = api_manager.user_steps.account_transfer(create_user_request, account_transfer_request)

        assert account_transfer_request.fromAccountId == response.fromAccountId
        assert account_transfer_request.toAccountId == response.toAccountId
        assert response.fromAccountIdBalance == account_create_with_balance.balance - 1000


    def test_account_transfer_invalid_422(self, api_manager, create_user_request):
        create_account_credit_1 = api_manager.user_steps.create_account(create_user_request)
        create_account_credit_2 = api_manager.user_steps.create_account(create_user_request)

        account_transfer_request = AccountTransferRequest(fromAccountId=create_account_credit_1.id,
                                                          toAccountId=create_account_credit_2.id,
                                                          amount=1000)

        api_manager.user_steps.account_transfer_invalid_422(create_user_request, account_transfer_request)