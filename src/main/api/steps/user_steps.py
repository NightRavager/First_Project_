from src.main.api.foundation.endpoint import Endpoint
from src.main.api.foundation.requesters.validate_crud_requester import ValidateCrudRequester
from src.main.api.foundation.requesters.crud_requester import CrudRequester
from src.main.api.models.account_deposit_request_valid import AccountDepositRequestValid
from src.main.api.models.account_transfer_request import AccountTransferRequest
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.specs.request_specs import RequestSpecs
from src.main.api.specs.response_specs import ResponseSpecs
from src.main.api.steps.base_steps import BaseSteps



class UserSteps(BaseSteps):
    @staticmethod
    def create_account(create_user_request: CreateUserRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.CREATE_ACCOUNT,
            ResponseSpecs.request_created()
        ).post()
        return response

    @staticmethod
    def account_deposit(create_user_request: CreateUserRequest, account_deposit_request: AccountDepositRequestValid):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.ACCOUNT_DEPOSIT,
            ResponseSpecs.request_ok()
        ).post(account_deposit_request)
        return response

    @staticmethod
    def account_transfer(create_user_request: CreateUserRequest, account_transfer_request: AccountTransferRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.ACCOUNT_TRANSFER,
            ResponseSpecs.request_ok()
        ).post(account_transfer_request)
        return response

    @staticmethod
    def account_transfer_invalid_422(create_user_request: CreateUserRequest, account_transfer_request: AccountTransferRequest):
        CrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.ACCOUNT_TRANSFER,
            ResponseSpecs.request_unprocessable_entity()
        ).post(account_transfer_request)

    @staticmethod
    def account_deposit_invalid_404(create_user_request: CreateUserRequest, account_deposit_request):
        CrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.ACCOUNT_DEPOSIT,
            ResponseSpecs.request_not_found()
        ).post(account_deposit_request)
