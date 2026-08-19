from http import HTTPStatus
from src.main.api.models.create_user_response import CreateUserResponse
from src.main.api.models.login_user_response import LoginUserResponse
from src.main.api.requsets.requester import Requester
from requests import Response
from src.main.api.models.login_user_request import LoginUserRequest
import requests


class LoginUserRequester(Requester):
    def post(self, login_user_request: LoginUserRequest) -> LoginUserResponse | Response:
        url=f"{self.base_url}/auth/token/login"
        response=requests.post(
            url=url,
            json= login_user_request.model_dump(),
            headers=self.headers
        )
        return LoginUserResponse(**response.json())

