import requests

BASE_URL = 'https://restful-booker.herokuapp.com'


class BaseClient:
    """Базовый класс для API-клиентов."""

    DEFAULT_HEADERS = {'Content-Type': 'application/json'}

    def __init__(self):
        """Дефолтные url и заголовок."""
        self.base_url = BASE_URL
        self.default_headers = self.DEFAULT_HEADERS


class AuthClient(BaseClient):
    """Базовый класс для автризации клиента."""

    def request(
        self,
        payload: dict,
        method: str = 'POST',
        headers: dict = {},
    ) -> requests.Response:
        """Отправка запроса."""
        return requests.request(
            method,
            url=f'{BASE_URL}/auth',
            json=payload,
            headers=dict(self.DEFAULT_HEADERS, **headers),
        )


auth_client = AuthClient()
