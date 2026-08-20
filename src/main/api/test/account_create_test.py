import pytest
from sqlalchemy.orm import Session

from src.classes.api_manager import ApiManager
from src.main.api.db.crud.account_crud import AccountCrudDb as Account
from src.main.api.models.create_user_request import CreateUserRequest


@pytest.mark.api
class TestAccountCreate:
    def test_account_create(self, db_session: Session, api_manager: ApiManager, create_user_request: CreateUserRequest):
        response = api_manager.user_steps.create_account(create_user_request)
        assert response.balance == 0

        account_from_db = Account.get_account_by_id(db_session, response.id)
        assert account_from_db.id == response.id, 'Аккаунт не создан, id нет в БД'
        assert account_from_db.balance is not None, "Поле баланса при создании аккаунта отсутствует в БД"


    '''def test_account_create_credit(self,api_manager, create_user_credit_request):
        response_account = api_manager.user_credit_steps.create_account_credit(create_user_credit_request)

        assert response_account.balance == 0'''





