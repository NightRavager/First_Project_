import pytest
from requests import Session

from api.models.account_create import AccountCreate
from api.models.account_deposit_request_valid import AccountDepositRequestValid
from src.classes.api_manager import ApiManager
from src.main.api.db.crud.account_crud import AccountCrudDb as Account


@pytest.mark.api
class TestAccountDeposit:
    def test_account_deposit(self, db_session: Session,
                             api_manager: ApiManager,
                             account_create: AccountCreate,
                             account_deposit_request: AccountDepositRequestValid):

        response = api_manager.user_steps.account_deposit(account_create.create_user_request,account_deposit_request)

        assert response.balance == account_deposit_request.amount, 'Депозит не внесен. Баланс получателя не равен сумме депозита'

        deposit_from_db = Account.get_account_by_id(db_session, response.id)

        assert deposit_from_db is not None, (
            f"Депозит с id={response.id} не найден в БД"
        )

        assert deposit_from_db.balance == account_deposit_request.amount, "Депозит не соответствует сумме запроса"


    def test_account_deposit_invalid_404(self, api_manager: ApiManager,
                                         account_create: AccountCreate,
                                         account_deposit_request: AccountDepositRequestValid):
        account_deposit_request.accountId += 1
        api_manager.user_steps.account_deposit_invalid_404(account_create.create_user_request,account_deposit_request)
