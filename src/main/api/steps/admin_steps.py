from src.main.api.foundation.endpoint import Endpoint
from src.main.api.foundation.requesters.crud_requester import CrudRequester
from src.main.api.foundation.requesters.validate_crud_requester import ValidateCrudRequester
from src.main.api.models.create_user_credit_request import CreateUserCreditRequest
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.login_user_request import LoginUserRequest
from src.main.api.specs.request_specs import RequestSpecs
from src.main.api.specs.response_specs import ResponseSpecs
from src.main.api.steps.base_steps import BaseSteps
from src.main.api.utils.constants import UserInfo


class AdminSteps(BaseSteps):
    def create_user(self, create_user_request: CreateUserRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=UserInfo.ADMIN_USERNAME, password=UserInfo.ADMIN_PASSWORD),
            Endpoint.ADMIN_CREATE_USER,
            ResponseSpecs.request_ok()
        ).post(create_user_request)

        self.created_obj.append(response)
        return response

    @staticmethod
    def delete_user(user_id: int):
        CrudRequester(
            RequestSpecs.auth_headers(username=UserInfo.ADMIN_USERNAME, password=UserInfo.ADMIN_PASSWORD),
            Endpoint.ADMIN_DELETE_USER,
            ResponseSpecs.request_ok()
        ).delete(user_id)

    @staticmethod
    def create_invalid_user(create_user_request: CreateUserRequest):
        CrudRequester(
            RequestSpecs.auth_headers(username=UserInfo.ADMIN_USERNAME, password=UserInfo.ADMIN_PASSWORD),
            Endpoint.ADMIN_CREATE_USER,
            ResponseSpecs.request_bad()
        ).post(create_user_request)

    @staticmethod
    def login_user(login_user_request: LoginUserRequest):
        response = ValidateCrudRequester(
            RequestSpecs.un_auth_headers(),
            Endpoint.LOGIN_USER,
            ResponseSpecs.request_ok()
        ).post(login_user_request)
        return response

    def create_user_credit(self, create_user_credit_request: CreateUserCreditRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=UserInfo.ADMIN_USERNAME, password=UserInfo.ADMIN_PASSWORD),
            Endpoint.ADMIN_CREATE_USER_CREDIT,
            ResponseSpecs.request_ok()
        ).post(create_user_credit_request)

        self.created_obj.append(response)
        return response

    def admin_users_delete(self, user_id: int):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=UserInfo.ADMIN_USERNAME, password=UserInfo.ADMIN_PASSWORD),
            Endpoint.ADMIN_USERS_DELETE,
            ResponseSpecs.request_ok()
        ).delete(user_id)
        self.created_obj.append(response)
        return response