import pytest

from src.main.api.models.admin_credentials import AdminCredentials


@pytest.fixture
def admin_credentials():
    admin_credentials = AdminCredentials(username = "admin", password = "123456")
    return admin_credentials