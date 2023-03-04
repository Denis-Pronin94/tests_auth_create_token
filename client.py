from typing import Optional

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


class BaseBookingClient(BaseClient):
    """Базовый класс для получения информации о бронировании."""

    BOOKING_URL = f'{BASE_URL}/booking'


class GetBookingClient(BaseBookingClient):
    """Базовый класс для получения информации о бронирования."""

    def request(
        self,
        method: str = 'GET',
        booking_id: Optional[str] = None,
    ) -> requests.Response:
        """Отправка запроса."""
        booking_id = booking_id or '1'
        return requests.request(
            method,
            url=f'{self.BOOKING_URL}/{booking_id}',
        )


class GetBookingIdsClient(BaseBookingClient):
    """Базовый класс для получения id бронирования."""

    def request(
        self,
        method: str = 'GET',
        params: Optional[dict] = None,
    ) -> requests.Response:
        """Отправка запроса."""
        return requests.request(
            method,
            url=f'{self.BOOKING_URL}',
            params=params,
        )


auth_client = AuthClient()
get_booking = GetBookingClient()
get_booking_ids = GetBookingIdsClient()
