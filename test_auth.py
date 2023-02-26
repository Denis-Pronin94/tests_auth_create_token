from http import HTTPStatus

import pytest

import requests


class TestAuth:
    """Сьют - авторизация."""

    BASE_URL = 'https://restful-booker.herokuapp.com'

    def send_auth_request(
            self,
            user_name: str = 'admin',
            password: str = 'password123',
            headers: dict = {'Content-Type': 'application/json'},
    ) -> requests.Response:
        """Функция отправки запроса на авторизацию."""
        payload = {
            "username": user_name,
            "password": password,
        }

        return requests.post(
            f'{self.BASE_URL}/auth',
            data=headers,
            json=payload,
        )

    @pytest.fixture
    def send_auth_request_fixture(self) -> requests.Response:
        """Отправка запроса на авторизацию - получения токена."""
        payload = {
            "username": "admin",
            "password": "password123",
        }
        return requests.post(
            url=f'{self.BASE_URL}/auth',
            json=payload,
        )

    def test_success_get_token(self, send_auth_request_fixture: requests.Response):
        """Позитивный тест - проверка получения токена."""
        response = send_auth_request_fixture

        assert response.status_code == HTTPStatus.OK
        assert 'token' in response.json()

    def test_check_token(self, send_auth_request_fixture: requests.Response):
        """Позитивный тест - проверка токена."""
        response = send_auth_request_fixture
        token = response.json()['token']
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Cookie': f'token={token}',
        }
        body = {
            'firstname': 'James',
            'lastname': 'Brown',
            'totalprice': 111,
            'depositpaid': True,
            'bookingdates': {
                'checkin': '2018-01-01',
                'checkout': '2019-01-01',
            },
            'additionalneeds': 'Breakfast',
        }
        response = requests.put(
            url=f'{self.BASE_URL}/booking/1',
            json=body,
            headers=headers,
        )

        assert response.status_code == HTTPStatus.OK

    @pytest.mark.parametrize(
        'user_name, password',
        [
            ('admin', '!!!!!!!!!'),
            ('!!!!!!!!!', 'password123'),
            (' adm in ', ' passw ord123 '),
            ('!@#$%,.admin', '!@#$%,.password123'),
            ('ADmin', 'PAssword123'),
            ('админ', 'пароль123'),
            ('admin123', 'password123'),
        ],
    )
    def test_wrong_credential(self, user_name: str, password: str):
        """Негативные тесты - отправка запроса с неправильными данными."""
        headers = {'Content-Type': 'application/json'}

        payload = {
            'username': user_name,
            'password': password,
        }

        response = requests.post(
            f'{self.BASE_URL}/auth',
            headers=headers,
            json=payload,
        )

        assert response.status_code == HTTPStatus.OK
        assert response.json() == {'reason': 'Bad credentials'}

    @pytest.mark.parametrize(
        'payload',
        [
            {'username': 'admin'},
            {'password': 'password123'},
            {'user_name': 'admin'},
            {},
        ],
    )
    def test_wrong_body(self, payload: str):
        """Негативные тесты - отправка запроса с неправильным телом."""
        headers = {'Content-Type': 'application/json'}

        response = requests.post(
            f'{self.BASE_URL}/auth',
            headers=headers,
            json=payload,
        )

        assert response.status_code == HTTPStatus.OK
        assert response.json() == {'reason': 'Bad credentials'}

    @pytest.mark.parametrize(
        'method',
        [
            'put',
            'get',
            'patch',
            'delete',
        ],
    )
    def test_wrong_method(self, method: str):
        """Негативные тесты - отправка запроса с неправильным методом."""
        headers = {'Content-Type': 'application/json'}

        payload = {
            'username': 'admin',
            'password': 'password123',
        }

        response = requests.request(
            method,
            f'{self.BASE_URL}/auth',
            headers=headers,
            json=payload,
        )

        assert response.status_code == HTTPStatus.NOT_FOUND

    @pytest.mark.parametrize(
        'headers',
        [
            {'Content-Type': 'text/plain'},
            {'Content-Type': 'image/svg+xml'},
            {'Content-Type': 'text/javascript; charset=utf-8'},
        ],
    )
    def test_wrong_headers(self, headers: str):
        """Негативные тесты - отправка запроса с неправильным заголовком."""
        payload = {
            'username': 'admin',
            'password': 'password123',
        }

        response = requests.post(
            f'{self.BASE_URL}/auth',
            headers=headers,
            json=payload,
        )

        assert response.status_code == HTTPStatus.OK
        assert response.json() == {'reason': 'Bad credentials'}
