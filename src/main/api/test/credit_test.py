import pytest
from requests import Session

from api.models.create_creadit_response import CreateCreditResponse
from api.models.create_user_credit_request import CreateUserCreditRequest
from api.models.user_credit_account_create import UserCreditAccountCreate
from src.classes.api_manager import ApiManager
from src.main.api.models.create_credit_request import CreateCreditRequest
from src.main.api.models.credit_repay_request import CreditRepayRequest
from src.main.api.utils.constants import CreditData
from src.main.api.db.crud.credit_crud import CreditCrudDb as Credit


@pytest.mark.api
class TestCredit:
    def test_credit_request(self, db_session: Session,
                            api_manager: ApiManager,
                            user_credit_account_create: UserCreditAccountCreate):
        create_credit_request = CreateCreditRequest(accountId=user_credit_account_create.response.id,
                                                    amount=CreditData.DEFAULT_AMOUNT_BALANCE,
                                                    termMonths=CreditData.DEFAULT_TERM_MONTHS)
        response = api_manager.user_credit_steps.create_credit(user_credit_account_create.create_user_credit_request,
                                                    create_credit_request)

        assert create_credit_request.amount == response.amount, 'Сумма кредита не соответствует запросу'

        credit_from_db = Credit.get_credit_by_credit_id(db_session, response.creditId)

        assert credit_from_db is not None, f"Кредит id={response.creditId} не найден в БД по creditId запроса"

        assert credit_from_db.id == response.creditId, "Кредит не найден в БД по creditId запроса"
        assert credit_from_db.amount == response.amount, "Сумма кредита в БД не соответствует запросу"
        assert credit_from_db.term_months == response.termMonths, "Срок кредита в БД не соответствует запросу"



    def test_credit_repay(self, db_session: Session,
                          api_manager: ApiManager,
                          create_user_credit_request: CreateUserCreditRequest,
                          create_account_credit_request: CreateCreditResponse,
                          amount: int = CreditData.DEFAULT_AMOUNT_BALANCE):

        credit_repay_request = CreditRepayRequest(accountId=create_account_credit_request.id,
                                                  creditId=create_account_credit_request.creditId,
                                                  amount=amount)
        response = api_manager.user_credit_steps.credit_repay(create_user_credit_request, credit_repay_request)

        assert credit_repay_request.creditId == response.creditId, 'Id кредита не соответствует'
        assert amount == response.amountDeposited, 'Сумма запроса не равна сумме депозита'

        credit_from_db = Credit.get_credit_by_credit_id(db_session, response.creditId)

        assert credit_from_db is not None, f"Кредит id={response.creditId} не найден в БД по creditId запроса"

        assert credit_from_db.amount == response.amountDeposited, "Задолженность по кредиту в БД не соответствует ответу"


    def test_credit_request_invalid_404(self, api_manager: ApiManager,
                                        user_credit_account_create: UserCreditAccountCreate):
        credit_request = CreateCreditRequest(accountId=user_credit_account_create.response.id+1,
                                             amount=CreditData.DEFAULT_AMOUNT_BALANCE,
                                             termMonths=CreditData.DEFAULT_TERM_MONTHS)
        api_manager.user_credit_steps.create_credit_invalid_404(user_credit_account_create.create_user_credit_request, credit_request)




    def test_credit_repay_invalid_422(self, api_manager: ApiManager,
                                      create_user_credit_request: CreateUserCreditRequest,
                                      create_account_credit_request: CreateCreditResponse,
                                      amount = CreditData.DEFAULT_AMOUNT_TRANSACTION):
        credit_repay_request = CreditRepayRequest(accountId=create_account_credit_request.id,
                                                  creditId=create_account_credit_request.creditId,
                                                  amount=amount)

        api_manager.user_credit_steps.credit_repay_invalid_422(create_user_credit_request, credit_repay_request)