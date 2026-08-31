import pytest
from requests import Session
from api.models.create_user_credit_request import CreateUserCreditRequest
from api.utils.constants import CreditData
from src.classes.api_manager import ApiManager
from src.main.api.models.account_transfer_request import AccountTransferRequest
from src.main.api.db.crud.transaction_crud import TransactionCrudDb as Transaction


@pytest.mark.api
class TestTransfer:
    def test_account_transfer(self, db_session: Session,
                              api_manager: ApiManager,
                              create_user_request: CreateUserCreditRequest,
                              account_create_with_balance,
                              account_create):
        account_transfer_request = AccountTransferRequest(fromAccountId=account_create_with_balance.id,
                                                          toAccountId=account_create.response.id,
                                                          amount=CreditData.DEFAULT_AMOUNT_TRANSACTION)

        response = api_manager.user_steps.account_transfer(create_user_request, account_transfer_request)

        assert account_transfer_request.fromAccountId == response.fromAccountId, 'Id отправителя не соответствует изначальному'
        assert account_transfer_request.toAccountId == response.toAccountId, 'Id получателя не соответствует изначальному'
        assert response.fromAccountIdBalance == account_create_with_balance.balance - CreditData.DEFAULT_AMOUNT_TRANSACTION, 'Изменения в балансе отправителя не совпадают'

        account_from_db = Transaction.get_transaction_by_from_account_id(db_session, response.fromAccountId)

        assert account_from_db is not None, f"Трансфер с id={response.fromAccountId} не найден в БД"

        assert account_from_db.from_account_id == response.fromAccountId, f"id={response.fromAccountId} отсутствует в БД"
        assert account_from_db.to_account_id == response.toAccountId, f"id={response.fromAccountId} отсутствует в БД"
        assert account_from_db.amount == CreditData.DEFAULT_AMOUNT_TRANSACTION, f"Сумма перевода не соответствует сумме запроса"


    def test_account_transfer_invalid_422(self, api_manager, create_user_request):
        create_account_credit_1 = api_manager.user_steps.create_account(create_user_request)
        create_account_credit_2 = api_manager.user_steps.create_account(create_user_request)

        account_transfer_request = AccountTransferRequest(fromAccountId=create_account_credit_1.id,
                                                          toAccountId=create_account_credit_2.id,
                                                          amount=CreditData.DEFAULT_AMOUNT_TRANSACTION)

        api_manager.user_steps.account_transfer_invalid_422(create_user_request, account_transfer_request)