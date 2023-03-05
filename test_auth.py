from http import HTTPStatus


from client import auth_client

import pytest


import requests


class TestAuth:
    """Сьют - авторизация."""

    @pytest.mark.skip(reason='Эта функция нужна для скипнутого теста')
    def send_auth_request(
        self,
        payload_fixture: dict,
        headers: dict = {'Content-Type': 'application/json'},
    ) -> requests.Response:
        """Функция отправки запроса на авторизацию."""
        payload = payload_fixture

        return requests.post(
            f'{self.BASE_URL}/auth',
            data=headers,
            json=payload,
        )

    @pytest.mark.skip(reason='Эта функция нужна для скипнутого теста')
    @pytest.fixture
    def send_auth_request_fixture(self, payload_fixture: dict) -> requests.Response:
        """Отправка запроса на авторизацию - получения токена."""
        payload = payload_fixture
        return requests.post(
            url=f'{self.BASE_URL}/auth',
            json=payload,
        )

    @pytest.fixture
    def payload_fixture(self) -> dict:
        """Получением тело запроса."""
        return {
            "username": "admin",
            "password": "password123",
        }

    def test_success_get_token(self, payload_fixture: dict):
        """Позитивный тест - проверка получения токена."""
        response = auth_client.request(payload=payload_fixture)

        assert response.status_code == HTTPStatus.OK
        assert 'token' in response.json()

    @pytest.mark.skip(reason='Не готов клиент на UpdateBooking')
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
    def test_wrong_credentials(self, user_name: str, password: str):
        """Негативные тесты - отправка запроса с неправильными данными."""
        payload = {
            'username': user_name,
            'password': password,
        }

        response = auth_client.request(payload)

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
    def test_wrong_payload_schema(self, payload: str):
        """Негативные тесты - отправка запроса с неправильным телом."""
        response = auth_client.request(payload)

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
    def test_wrong_method(self, payload_fixture: dict, method: str):
        """Негативные тесты - отправка запроса с неправильным методом."""
        response = auth_client.request(payload=payload_fixture, method=method)

        assert response.status_code == HTTPStatus.NOT_FOUND

    @pytest.mark.parametrize(
        'headers',
        [
            {'Content-Type': 'text/plain'},
            {'Content-Type': 'image/svg+xml'},
            {'Content-Type': 'text/javascript; charset=utf-8'},
        ],
    )
    def test_wrong_headers(self, payload_fixture: dict, headers: str):
        """Негативные тесты - отправка запроса с неправильным заголовком."""
        response = auth_client.request(payload=payload_fixture, headers=headers)

        assert response.status_code == HTTPStatus.OK
        assert response.json() == {'reason': 'Bad credentials'}
