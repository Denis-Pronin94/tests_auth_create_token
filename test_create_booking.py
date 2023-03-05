from http import HTTPStatus

from client import create_booking

import pytest


class TestCreateBooking:
    """Сьют - создание бронирования."""

    @pytest.mark.parametrize(
        'payload',
        [
            {
                'firstname': 'Jim',
                'lastname': 'Brown',
                'totalprice': 111,
                'depositpaid': True,
                'bookingdates': {
                    'checkin': '2018-01-01',
                    'checkout': '2019-01-01',
                },
                'additionalneeds': 'Breakfast',
            },
            {
                'firstname': 'Jimmmmmmmm',
                'lastname': 'Brownnnnnnnnnnnn',
                'totalprice': 99999999999,
                'depositpaid': False,
                'bookingdates': {
                    'checkin': '2016-01-01',
                    'checkout': '2022-01-01',
                },
                'additionalneeds': 'Breakfasttttttttttt',
            },
        ],
    )
    def test_positive(self, payload: dict):
        """Позитивные тесты."""
        response = create_booking.request(payload=payload)

        assert response.status_code == HTTPStatus.OK
        assert 'bookingid', 'booking' in response.json()
        assert ['bookingid'] == int or float
        assert 'firstname', 'lastname' in response.json()
        assert 'totalprice', 'depositpaid' in response.json()
        assert ['totalprice'] == int or float
        assert 'bookingdates', 'checkin' in response.json()
        assert 'checkout', 'additionalneeds' in response.json()

    @pytest.fixture
    def payload_fixture(self) -> dict:
        """Получение тела запроса."""
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
    def test_wrong_method(self, method: str, payload_fixture: dict):
        """Негативные тесты - неправильный метод."""
        response = create_booking.request(method=method, payload=payload_fixture)

        assert response.status_code == HTTPStatus.NOT_FOUND

    @pytest.mark.parametrize(
        'payload',
        [
            {
                'lastname': 'Brown',
                'totalprice': 111,
                'depositpaid': True,
                'bookingdates': {
                    'checkin': '2018-01-01',
                    'checkout': '2019-01-01',
                },
                'additionalneeds': 'Breakfast',
            },
            {
                'firstname': 'Jim',
                'totalprice': 111,
                'depositpaid': True,
                'bookingdates': {
                    'checkin': '2018-01-01',
                    'checkout': '2019-01-01',
                },
                'additionalneeds': 'Breakfast',
            },
            {
                'firstname': 'Jim',
                'lastname': 'Brown',
                'depositpaid': True,
                'bookingdates': {
                    'checkin': '2018-01-01',
                    'checkout': '2019-01-01',
                },
                'additionalneeds': 'Breakfast',
            },
            {
                'firstname': 'Jim',
                'lastname': 'Brown',
                'totalprice': 111,
                'bookingdates': {
                    'checkin': '2018-01-01',
                    'checkout': '2019-01-01',
                },
                'additionalneeds': 'Breakfast',
            },
            {
                'firstname': 'Jim',
                'lastname': 'Brown',
                'totalprice': 111,
                'depositpaid': True,
                'additionalneeds': 'Breakfast',
            },
            {
                'firstname': 'Jim',
                'lastname': 'Brown',
                'totalprice': 111,
                'depositpaid': True,
                'bookingdates': {
                    'checkout': '2019-01-01',
                },
                'additionalneeds': 'Breakfast',
            },
            {
                'firstname': 'Jim',
                'lastname': 'Brown',
                'totalprice': 111,
                'depositpaid': True,
                'bookingdates': {
                    'checkin': '2018-01-01',
                },
                'additionalneeds': 'Breakfast',
            },
            {
                'firstname': 'Jim',
                'lastname': 'Brown',
                'totalprice': 111,
                'depositpaid': True,
                'bookingdates': {
                    'checkin': '2018-01-01',
                    'checkout': '2019-01-01',
                },
            },
        ],
    )
    def test_no_parameter(self, payload: dict):
        """Негативные тесты - отсутствие параметров."""
        response = create_booking.request(payload=payload)

        assert response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR

    @pytest.mark.parametrize(
        'payload',
        [
            {
                'firstname': 123,
                'lastname': 'Brown',
                'totalprice': 111,
                'depositpaid': True,
                'bookingdates': {
                    'checkin': '2018-01-01',
                    'checkout': '2019-01-01',
                },
                'additionalneeds': 'Breakfast',
            },
            {
                'firstname': 'Jim',
                'lastname': 123,
                'totalprice': 111,
                'depositpaid': True,
                'bookingdates': {
                    'checkin': '2018-01-01',
                    'checkout': '2019-01-01',
                },
                'additionalneeds': 'Breakfast',
            },
            {
                'firstname': 'Jim',
                'lastname': 'Brown',
                'totalprice': '111',
                'depositpaid': True,
                'bookingdates': {
                    'checkin': '2018-01-01',
                    'checkout': '2019-01-01',
                },
                'additionalneeds': 'Breakfast',
            },
            {
                'firstname': 'Jim',
                'lastname': 'Brown',
                'totalprice': 111,
                'depositpaid': 'True',
                'bookingdates': {
                    'checkin': '2018-01-01',
                    'checkout': '2019-01-01',
                },
                'additionalneeds': 'Breakfast',
            },
            {
                'firstname': 'Jim',
                'lastname': 'Brown',
                'totalprice': 111,
                'depositpaid': True,
                'bookingdates': {
                    'checkin': 'Jim',
                    'checkout': '2019-01-01',
                },
                'additionalneeds': 'Breakfast',
            },
            {
                'firstname': 'Jim',
                'lastname': 'Brown',
                'totalprice': 111,
                'depositpaid': True,
                'bookingdates': {
                    'checkin': '2018-01-01',
                    'checkout': 'Brown',
                },
                'additionalneeds': 'Breakfast',
            },
            {
                'firstname': 'Jim',
                'lastname': 'Brown',
                'totalprice': 111,
                'depositpaid': True,
                'bookingdates': {
                    'checkin': '2018-01-01',
                    'checkout': '2019-01-01',
                },
                'additionalneeds': 123,
            },
            {
                'firstname': True,
                'lastname': 'Brown',
                'totalprice': 111,
                'depositpaid': True,
                'bookingdates': {
                    'checkin': '2018-01-01',
                    'checkout': '2019-01-01',
                },
                'additionalneeds': 'Breakfast',
            },
            {
                'firstname': 'Jim',
                'lastname': False,
                'totalprice': 111,
                'depositpaid': True,
                'bookingdates': {
                    'checkin': '2018-01-01',
                    'checkout': '2019-01-01',
                },
                'additionalneeds': 'Breakfast',
            },
            {
                'firstname': 'Jim',
                'lastname': 'Brown',
                'totalprice': True,
                'depositpaid': True,
                'bookingdates': {
                    'checkin': '2018-01-01',
                    'checkout': '2019-01-01',
                },
                'additionalneeds': 'Breakfast',
            },
            {
                'firstname': 'Jim',
                'lastname': 'Brown',
                'totalprice': 111,
                'depositpaid': True,
                'bookingdates': {
                    'checkin': True,
                    'checkout': '2019-01-01',
                },
                'additionalneeds': 'Breakfast',
            },
            {
                'firstname': 'Jim',
                'lastname': 'Brown',
                'totalprice': 111,
                'depositpaid': True,
                'bookingdates': {
                    'checkin': '2018-01-01',
                    'checkout': 'False',
                },
                'additionalneeds': 'Breakfast',
            },
            {
                'firstname': 'Jim',
                'lastname': 'Brown',
                'totalprice': 111,
                'depositpaid': True,
                'bookingdates': {
                    'checkin': '2018-01-01',
                    'checkout': '2019-01-01',
                },
                'additionalneeds': True,
            },
        ],
    )
    def test_wrong_value(self, payload: dict):
        """Негативные тесты - отсутствие параметров."""
        response = create_booking.request(payload=payload)

        assert response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR
