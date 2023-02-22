from http import HTTPStatus

import pytest
import requests


class TestAuth:

    @pytest.fixture
    def send_auth_request(self) -> requests.Response:
        json = {
            "username": "admin",
            "password": "password123"
        }
        return requests.post(
            url='https://restful-booker.herokuapp.com/auth',
            json=json,
        )

    def test_success_get_token(self, send_auth_request):
        response = send_auth_request

        assert response.status_code == HTTPStatus.OK
        assert 'token' in response.json()

    def test_check_token(self, send_auth_request):
        response = send_auth_request
        token = response.json()['token']
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Cookie': f'token={token}'
        }
        body = {
            'firstname': 'James',
            'lastname': 'Brown',
            'totalprice': 111,
            'depositpaid': True,
            'bookingdates': {
                'checkin': '2018-01-01',
                'checkout': '2019-01-01'
            },
            'additionalneeds': 'Breakfast'
        }
        response = requests.put(
            'https://restful-booker.herokuapp.com/booking/1',
            json=body,
            headers=headers,
        )

        assert response.status_code == HTTPStatus.OK
