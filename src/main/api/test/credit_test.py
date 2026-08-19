import pytest

from src.main.api.models.create_credit_request import CreateCreditRequest
from src.main.api.models.credit_repay_request import CreditRepayRequest


@pytest.mark.api
class TestCredit:
    def test_credit_request(self,api_manager, create_user_credit_request):
        response_account = api_manager.user_credit_steps.create_account_credit(create_user_credit_request)

        credit_request = CreateCreditRequest(accountId=response_account.id, amount=5000, termMonths=12)
        response = api_manager.user_credit_steps.create_credit(create_user_credit_request, credit_request)

        assert credit_request.accountId == response.id
        assert credit_request.amount == response.amount


    def test_credit_repay(self,api_manager, create_user_credit_request):
        response_account = api_manager.user_credit_steps.create_account_credit(create_user_credit_request)

        credit_request = CreateCreditRequest(accountId=response_account.id, amount=5000, termMonths=12)
        credit_response = api_manager.user_credit_steps.create_credit(create_user_credit_request, credit_request)
        credit_repay_request = CreditRepayRequest(accountId=credit_response.id, creditId=credit_response.creditId, amount=5000)
        response = api_manager.user_credit_steps.credit_repay(create_user_credit_request, credit_repay_request)

        assert credit_response.creditId == response.creditId
        assert credit_response.amount == response.amountDeposited


    def test_credit_request_invalid(self,api_manager, create_user_credit_request):
        response_account = api_manager.user_credit_steps.create_account_credit(create_user_credit_request)

        credit_request = CreateCreditRequest(accountId=response_account.id+1, amount=5000, termMonths=12)


        api_manager.user_credit_steps.create_credit_invalid(create_user_credit_request, credit_request)



    def test_credit_repay_invalid(self,api_manager, create_user_credit_request):
        response_account = api_manager.user_credit_steps.create_account_credit(create_user_credit_request)

        credit_request = CreateCreditRequest(accountId=response_account.id, amount=5000, termMonths=12)
        credit_response = api_manager.user_credit_steps.create_credit(create_user_credit_request, credit_request)
        credit_repay_request = CreditRepayRequest(accountId=credit_response.id, creditId=credit_response.creditId, amount=1000)

        api_manager.user_credit_steps.credit_repay_invalid(create_user_credit_request, credit_repay_request)