from src.main.api.fixtures.user_fixture import create_user_request
from src.main.api.foundation.endpoint import Endpoint
from src.main.api.foundation.requesters.validate_crud_requester import ValidateCrudRequester
from src.main.api.foundation.requesters.crud_requester import CrudRequester
from src.main.api.models.create_user_credit_request import CreateUserCreditRequest
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.credit_repay_request import CreditRepayRequest
from src.main.api.specs.request_specs import RequestSpecs
from src.main.api.specs.response_specs import ResponseSpecs
from src.main.api.steps.base_steps import BaseSteps
from src.main.api.models.create_credit_request import CreateCreditRequest



class UserCreditSteps(BaseSteps):
    @staticmethod
    def create_account_credit(create_user_credit_request: CreateUserRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_credit_request.username, password=create_user_credit_request.password),
            Endpoint.CREATE_ACCOUNT,
            ResponseSpecs.request_created()
        ).post()
        return response

    @staticmethod
    def create_credit(create_user_request: CreateUserCreditRequest, credit_request: CreateCreditRequest):

        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.REQUEST_CREDIT,
            ResponseSpecs.request_created()
        ).post(credit_request)
        return response

    @staticmethod
    def credit_repay(create_user_credit_request: CreateUserCreditRequest, credit_repay_request: CreditRepayRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_credit_request.username,
                                      password=create_user_credit_request.password, ),
            Endpoint.CREDIT_REPAY,
            ResponseSpecs.request_ok()
        ).post(credit_repay_request)
        return response

    @staticmethod
    def credit_repay_invalid_422(create_user_credit_request: CreateUserCreditRequest, credit_repay_request: CreditRepayRequest):
        CrudRequester(
            RequestSpecs.auth_headers(username=create_user_credit_request.username,
                                      password=create_user_credit_request.password, ),
            Endpoint.CREDIT_REPAY,
            ResponseSpecs.request_unprocessable_entity()
        ).post(credit_repay_request)

    @staticmethod
    def create_credit_invalid_404(create_user_credit_request: CreateUserCreditRequest, credit_request: CreateCreditRequest):
        CrudRequester(
            RequestSpecs.auth_headers(username=create_user_credit_request.username, password=create_user_credit_request.password,),
            Endpoint.REQUEST_CREDIT,
            ResponseSpecs.request_not_found()
        ).post(credit_request)
