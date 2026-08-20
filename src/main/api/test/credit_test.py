import pytest

from src.main.api.models.create_credit_request import CreateCreditRequest
from src.main.api.models.credit_repay_request import CreditRepayRequest


@pytest.mark.api
class TestCredit:
    def test_credit_request(self,api_manager, user_credit_account_create):
        create_credit_request = CreateCreditRequest(accountId=user_credit_account_create.response.id, amount=5000,
                                                    termMonths=12)
        response = api_manager.user_credit_steps.create_credit(user_credit_account_create.create_user_credit_request,
                                                    create_credit_request)
        assert create_credit_request.amount == response.amount



    def test_credit_repay(self,api_manager, create_user_credit_request, credit_request_fixture, amount = 5000):
        credit_repay_request = CreditRepayRequest(accountId=credit_request_fixture.create_credit_response.id,
                                                  creditId=credit_request_fixture.create_credit_response.creditId, amount=amount)
        response = api_manager.user_credit_steps.credit_repay(create_user_credit_request, credit_repay_request)

        assert credit_request_fixture.create_credit_response.creditId == response.creditId
        assert amount == response.amountDeposited


    def test_credit_request_invalid_404(self, api_manager, user_credit_account_create):
        credit_request = CreateCreditRequest(accountId=user_credit_account_create.response.id+1, amount=5000, termMonths=12)
        api_manager.user_credit_steps.create_credit_invalid_404(user_credit_account_create.create_user_credit_request, credit_request)




    def test_credit_repay_invalid_422(self,api_manager, create_user_credit_request, credit_request_fixture, amount = 2000):
        credit_repay_request = CreditRepayRequest(accountId=credit_request_fixture.create_credit_response.id,
                                                  creditId=credit_request_fixture.create_credit_response.creditId, amount=amount)

        api_manager.user_credit_steps.credit_repay_invalid_422(create_user_credit_request, credit_repay_request)