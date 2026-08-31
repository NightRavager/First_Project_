import pytest
from src.main.api.models.login_user_request import LoginUserRequest


@pytest.mark.api
class TestUserLogin:
    def test_login_admin(self, api_manager):
        login_user_request = LoginUserRequest(username="admin", password="123456")

        response = api_manager.admin_steps.login_user(login_user_request)

        assert login_user_request.username == response.user.username, "Имя пользователя в запросе и в ответе не совпадает"
        assert response.user.role == "ROLE_ADMIN", "Пользователь с ролью ROLE_ADMIN не создан"

    def test_login_user(self, api_manager, create_user_request):
        response = api_manager.admin_steps.login_user(create_user_request)

        assert create_user_request.username == response.user.username, "Имя пользователя в запросе и в ответе не совпадает"
        assert response.user.role == "ROLE_USER", "Пользователь с ролью ROLE_USER не создан"
