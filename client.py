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


class GetBooking(BaseClient):
    """Базовый класс для получения информации о бронировании."""

    def request(self, method: str = 'GET', booking_id: str = None) -> requests.Response:
        """Отправка запроса."""
        booking_id = booking_id or '1'
        return requests.request(
            method,
            url=f'{BASE_URL}/booking/{booking_id}',
        )


class GetBookingIds(BaseClient):
    """Базовый класс для получения id бронирования."""

    def request(self, method: str = 'GET', params: dict = None) -> requests.Response:
        """Отправка запроса."""
        return requests.request(
            method,
            url=f'{BASE_URL}/booking',
            params=params,
        )


auth_client = AuthClient()
get_booking = GetBooking()
get_booking_ids = GetBookingIds()
