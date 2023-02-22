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

    def test_error_path(self):
        response = requests.post('https://restful-booker.herokuapp.com/aut',
                                 'Content-Type: application/json',
                                 {
                                     "username": "admin",
                                     "password": "password123"
                                 }
                                 )

        assert response.status_code == HTTPStatus.NOT_FOUND

    def test_valid_user_name_and_not_valid_password(self):
        response = requests.post('https://restful-booker.herokuapp.com/auth',
                                 'Content-Type: application/json',
                                 {
                                     "username": "admin",
                                     "password": "!!!!!"
                                 }
                                 )

        assert response.status_code == HTTPStatus.OK
        assert 'reason' in response.json()

    def test_not_valid_user_name_and_valid_password(self):
        response = requests.post('https://restful-booker.herokuapp.com/auth',
                                 'Content-Type: application/json',
                                 {
                                     "username": "!!!!!",
                                     "password": "password123"
                                 }
                                 )

        assert response.status_code == HTTPStatus.OK
        assert 'reason' in response.json()

    def test_only_body_user_name(self):
        response = requests.post('https://restful-booker.herokuapp.com/auth',
                                 'Content-Type: application/json',
                                 {
                                     "username": "admin"
                                 }
                                 )

        assert response.status_code == HTTPStatus.OK
        assert 'reason' in response.json()

    def test_only_body_password(self):
        response = requests.post('https://restful-booker.herokuapp.com/auth',
                                 'Content-Type: application/json',
                                 {
                                     "password": "password123"
                                 }
                                 )

        assert response.status_code == HTTPStatus.OK
        assert 'reason' in response.json()

    def test_space_in_values(self):
        response = requests.post('https://restful-booker.herokuapp.com/auth',
                                 'Content-Type: application/json',
                                 {
                                     "username": " ad min ",
                                     "password": " passw ord123 "
                                 }
                                 )

        assert response.status_code == HTTPStatus.OK
        assert 'reason' in response.json()

    def test_symbol_in_values(self):
        response = requests.post('https://restful-booker.herokuapp.com/auth',
                                 'Content-Type: application/json',
                                 {
                                     "username": "/!#$.,+-=admin",
                                     "password": "password123/!#$.,+-="
                                 }
                                 )

        assert response.status_code == HTTPStatus.OK
        assert 'reason' in response.json()

    def test_register_in_values(self):
        response = requests.post('https://restful-booker.herokuapp.com/auth',
                                 'Content-Type: application/json',
                                 {
                                     "username": "PASSword123",
                                     "password": "ADmin"
                                 }
                                 )

        assert response.status_code == HTTPStatus.OK
        assert 'reason' in response.json()

    def test_another_language_in_values(self):
        response = requests.post('https://restful-booker.herokuapp.com/auth',
                                 'Content-Type: application/json',
                                 {
                                     "username": "админ",
                                     "password": "пароль123"
                                 }
                                 )

        assert response.status_code == HTTPStatus.OK
        assert 'reason' in response.json()

    def test_numbers_in_values(self):
        response = requests.post('https://restful-booker.herokuapp.com/auth',
                                 'Content-Type: application/json',
                                 {
                                     "username": "admin123",
                                     "password": "password123"
                                 }
                                 )

        assert response.status_code == HTTPStatus.OK
        assert 'reason' in response.json()

    def test_not_valid_content_type(self):
        response = requests.post('https://restful-booker.herokuapp.com/auth',
                                 'Content-Type: text/plain',
                                 {
                                     "username": "пароль123",
                                     "password": "админ"
                                 }
                                 )

        assert response.status_code == HTTPStatus.OK
        assert 'reason' in response.json()
