from http import HTTPStatus

from client import get_booking

import pytest


class TestGetBooking:
    """Сьют - получение информации о бронировании по id."""

    @pytest.mark.parametrize(
        'booking_id',
        [
            '1',
            '50',
        ],
    )
    def test_positive(self, booking_id: str):
        """Позитивные тесты."""
        response = get_booking.request(booking_id=booking_id)

        assert response.status_code == HTTPStatus.OK
        assert 'firstname', 'lastname' in response.json()
        assert 'totalprice', 'depositpaid' in response.json()
        assert 'bookingdates' in response.json()
        assert 'checkin', 'checkout' in response.json()

    @pytest.mark.parametrize(
        'booking_id',
        [
            '!',
            'qwerty',
            'йцукен',
            '99999',
        ],
    )
    def test_wrong_values(self, booking_id: str):
        """Негативные тесты - отправляем запрос с некорректными значениями."""
        response = get_booking.request(booking_id=booking_id)

        assert response.status_code == HTTPStatus.NOT_FOUND

    @pytest.mark.parametrize(
        'method',
        [
            'put',
            'delete',
            'patch',
        ],
    )
    def test_wrong_method(self, method: str):
        """Негативные тесты - отправляем запрос с неправильным методом."""
        response = get_booking.request(method=method)

        assert response.status_code == HTTPStatus.FORBIDDEN
