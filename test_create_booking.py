from http import HTTPStatus

from client import create_booking

import pytest

from test_data import ids_for_test_no_parameter, ids_test_positive, ids_test_wrong_value, \
    negative_type_in_data, no_parameter_in_data, valid_data


class TestCreateBooking:
    """Сьют - создание бронирования."""

    @pytest.mark.parametrize(
        'payload',
        valid_data,
        ids=ids_test_positive,
    )
    def test_positive(self, payload: dict):
        """Позитивные тесты."""
        response = create_booking.request(payload=payload)

        assert response.status_code == HTTPStatus.OK
        assert 'bookingid', 'booking' in response.json()
        assert type(response.json()['bookingid']) == int
        assert 'firstname', 'lastname' in response.json()
        assert 'totalprice', 'depositpaid' in response.json()
        assert type(response.json()['booking']['totalprice']) == int
        assert 'bookingdates', 'checkin' in response.json()
        assert 'checkout', 'additionalneeds' in response.json()

    @pytest.fixture
    def payload(self) -> dict:
        """Возвращает тело запроса для теста test_wrong_method."""
        return {
            'firstname': 'Jim',
            'lastname': 'Brown',
            'totalprice': 111,
            'depositpaid': True,
            'bookingdates': {
                'checkin': '2018-01-01',
                'checkout': '2019-01-01',
            },
            'additionalneeds': 'Breakfast',
        }

    @pytest.mark.parametrize(
        'method',
        [
            'get',
            'put',
            'delete',
            'patch',
        ],
    )
    def test_wrong_method(self, method: str, payload: dict):
        """Негативные тесты - отправляем запрос с неправильным методом."""
        response = create_booking.request(method=method, payload=payload)

        assert response.status_code == HTTPStatus.NOT_FOUND

    @pytest.mark.parametrize(
        'payload',
        no_parameter_in_data,
        ids=ids_for_test_no_parameter,
    )
    def test_no_parameter(self, payload: dict):
        """Негативные тесты - отправка запроса с отсутстующим параметром."""
        response = create_booking.request(payload=payload)

        assert response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR

    @pytest.mark.parametrize(
        'payload',
        negative_type_in_data,
        ids=ids_test_wrong_value,
    )
    def test_wrong_value(self, payload: dict):
        """Негативные тесты - отправка запроса с неправильным значением параметра."""
        response = create_booking.request(payload=payload)

        assert response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR
