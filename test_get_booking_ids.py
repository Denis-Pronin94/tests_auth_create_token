from http import HTTPStatus


from client import get_booking_ids

import pytest


class TestGetBookingIds:
    """Сьют - получение id бронирования."""

    @pytest.mark.parametrize(
        'params',
        [
            {},
            {
                'firstname': 'Josh',
                'lastname': 'Allen',
            },
            {
                'checkin': '2017-01-01',
                'checkout': '2020-01-01',
            },
            {
                'firstname': 'Josh',
                'lastname': 'Allen',
                'checkin': '2017-01-01',
                'checkout': '2020-01-01',
            },
            {
                'firstname': 'Josh',
                'checkout': '2020-01-01',
            },
            {
                'lastname': 'Allen',
                'checkin': '2017-01-01',
            },
        ],
    )
    def test_positive(self, params: dict):
        """Позитивные тесты."""
        response = get_booking_ids.request(params=params)

        assert response.status_code == HTTPStatus.OK
        for json_booking_id in response.json():
            assert 'bookingid' in json_booking_id
            assert json_booking_id['bookingid'] > 0
            assert type(json_booking_id['bookingid']) == int

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
        response = get_booking_ids.request(method=method)

        assert response.status_code == HTTPStatus.NOT_FOUND

    @pytest.mark.skip(reason='Баг - ответ должен быть BAD_REQUEST, а он 200 ОК')
    @pytest.mark.parametrize(
        'params',
        [
            {'': ''},
            {
                'totalprice': 'Allen',
            },
            {
                'lastname': 'Allgsfdsfdsen',
            },
            {
                'lastname': '2017-01-01',
            },
        ],
    )
    def test_wrong_params(self, params: dict):
        """Негативные тесты - отправляем запрос с неправильными параметрами."""
        response = get_booking_ids.request(params=params)

        assert response.status_code == HTTPStatus.BAD_REQUEST
