import requests

BASE_URL = 'https://restful-booker.herokuapp.com'


class BaseClient:
    """Класс - BaseClient."""

    DEFAULT_HEADERS = {'Content-Type': 'application/json'}

    def __init__(self):
        """Дефолтные url и заголовок."""
        self.base_url = BASE_URL
        self.default_headers = self.DEFAULT_HEADERS


class AuthClient(BaseClient):
    """Класс - AuthClient."""

    def request(self, payload: dict, method: str = None, headers: dict = None)\
            -> requests.Response:
        """Отправка запроса."""
        method = method or 'POST'

        return requests.request(
            method,
            url=f'{BASE_URL}/auth',
            json=payload,
            headers=dict(self.DEFAULT_HEADERS, **headers),
        )


auth_client = AuthClient()
