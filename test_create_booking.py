from http import HTTPStatus

from client import create_booking

import pytest

from test_data import additional_needs, additional_needs_bool, additional_needs_number, \
    booking_dates, checkin, checkin_bool, checkin_str, checkout, checkout_bool, checkout_str, \
    deposit_paid, deposit_paid_str, first_name_bool, first_name_number, firstname, \
    last_name_bool, last_name_number, lastname, positive_data_one, positive_data_two, \
    total_price, total_price_bool, total_price_str


class TestCreateBooking:
    """Сьют - создание бронирования."""

    @pytest.mark.parametrize(
        'payload',
        [
            positive_data_one,
            positive_data_two,
        ],
        ids=['Валидные значения', 'Валидные значения'],
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

    @pytest.mark.parametrize(
        'method',
        [
            'get',
            'put',
            'delete',
            'patch',
        ],
    )
    def test_wrong_method(self, method: str):
        """Негативные тесты - отправляем запрос с неправильным методом."""
        response = create_booking.request(method=method, payload=positive_data_one)

        assert response.status_code == HTTPStatus.NOT_FOUND

    @pytest.mark.parametrize(
        'payload',
        [
            firstname,
            lastname,
            total_price,
            deposit_paid,
            booking_dates,
            checkin,
            checkout,
            additional_needs,
        ],
        ids=[
            'Нет параметра firstname',
            'Нет параметра lastname',
            'Нет параметра totalprice',
            'Нет параметра depositpaid,',
            'Нет параметра bookingdates',
            'Нет параметра checkin',
            'Нет параметра checkout',
            'Нет параметра additionalneeds',
        ],
    )
    def test_no_parameter(self, payload: dict):
        """Негативные тесты - отправка запроса с отсутстующим параметром."""
        response = create_booking.request(payload=payload)

        assert response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR

    @pytest.mark.parametrize(
        'payload',
        [
            first_name_number,
            last_name_number,
            total_price_str,
            deposit_paid_str,
            checkin_str,
            checkout_str,
            additional_needs_number,
            first_name_bool,
            last_name_bool,
            total_price_bool,
            checkin_bool,
            checkout_bool,
            additional_needs_bool,
        ],
        ids=[
            'firstname - число',
            'lastname - число',
            'totalprice - строка',
            'depositpaid - строка',
            'checkin - строка',
            'checkout - строка',
            'additional_needs - число',
            'firstname - булевое значение',
            'lastname - булевое значение',
            'totalprice - булевое значение',
            'checkin - булевое значение',
            'checkout - булевое значение',
            'additionalneeds - булевое значение',
        ],
    )
    def test_wrong_value(self, payload: dict):
        """Негативные тесты - отправка запроса с неправильным значением параметра."""
        response = create_booking.request(payload=payload)

        assert response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR
