from http import HTTPStatus

import pytest

import requests


class TestAuth:
    """Сьют - авторизация."""

    BASE_URL = 'https://restful-booker.herokuapp.com'

    @pytest.fixture
    def send_auth_request(self) -> requests.Response:
        """Отправка запроса на авторизацию - получения токена."""
        json = {
            "username": "admin",
            "password": "password123",
        }
        return requests.post(
            url='https://restful-booker.herokuapp.com/auth',
            json=json,
        )

    def test_success_get_token(self, send_auth_request: requests.Response):
        """Позитивный тест - проверка получения токена."""
        response = send_auth_request

        assert response.status_code == HTTPStatus.OK
        assert 'token' in response.json()

    def test_check_token(self, send_auth_request: requests.Response):
        """Позитивный тест - проверка токена."""
        response = send_auth_request
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
            url=f'{self.BASE_URL}booking/1',
            json=body,
            headers=headers,
        )

        assert response.status_code == HTTPStatus.OK

    def test_error_path(self):
        """Негативный тест с ошибкой в пути."""
        response = requests.post(
            url=f'{self.BASE_URL}aut',
            headers={'Content-Type': 'application/json'},
            json={
                "username": "admin",
                "password": "password123",
            },
        )

        assert response.status_code == HTTPStatus.NOT_FOUND

    def test_valid_user_name_and_not_valid_password(self):
        """Негативный тест с валидным user_name и не валидным паролем."""
        response = requests.post(
            url=f'{self.BASE_URL}auth',
            headers={'Content-Type': 'application/json'},
            json={
                "username": "admin",
                "password": "!!!!!!",
            },
        )

        assert response.status_code == HTTPStatus.OK
        assert 'reason' in response.json()

    def test_not_valid_user_name_and_valid_password(self):
        """Негативный тест с невалидныйм user_name и валидным паролем."""
        response = requests.post(
            url=f'{self.BASE_URL}auth',
            headers={'Content-Type': 'application/json'},
            json={
                "username": "!!!!!!",
                "password": "password123",
            },
        )

        assert response.status_code == HTTPStatus.OK
        assert 'reason' in response.json()

    def test_only_body_user_name(self):
        """Негативный тест - в теле передаётся только user_name."""
        response = requests.post(
            url=f'{self.BASE_URL}auth',
            headers={'Content-Type': 'application/json'},
            json={"username": "admin"},
        )

        assert response.status_code == HTTPStatus.OK
        assert 'reason' in response.json()

    def test_only_body_password(self):
        """Негативный тест - в теле передаётся только пароль."""
        response = requests.post(
            url=f'{self.BASE_URL}auth',
            headers={'Content-Type': 'application/json'},
            json={"password": "password123"},
        )

        assert response.status_code == HTTPStatus.OK
        assert 'reason' in response.json()

    def test_space_in_values(self):
        """Негатиыный тест - в значениях присутствуют пробелы вначале, в середине и в конце."""
        response = requests.post(
            url=f'{self.BASE_URL}auth',
            headers={'Content-Type': 'application/json'},
            json={
                "username": " ad min ",
                "password": " passw ord123 ",
            },
        )

        assert response.status_code == HTTPStatus.OK
        assert 'reason' in response.json()

    def test_symbol_in_values(self):
        """Нагативный тест - в значениях присутствуют спец. символы."""
        response = requests.post(
            url=f'{self.BASE_URL}auth',
            headers={'Content-Type': 'application/json'},
            json={
                "username": "admin!@#$,.",
                "password": "!@#$,.password123",
            },
        )

        assert response.status_code == HTTPStatus.OK
        assert 'reason' in response.json()

    def test_register_in_values(self):
        """Негативный тест - в значениях пристутвует разный регистр."""
        response = requests.post(
            url=f'{self.BASE_URL}auth',
            headers={'Content-Type': 'application/json'},
            json={
                "username": "ADmin",
                "password": "PASsword123",
            },
        )

        assert response.status_code == HTTPStatus.OK
        assert 'reason' in response.json()

    def test_another_language_in_values(self):
        """Негативный тест - значения на другой языке."""
        response = requests.post(
            url=f'{self.BASE_URL}auth',
            headers={'Content-Type': 'application/json'},
            json={
                "username": "админ",
                "password": "пароль123",
            },
        )

        assert response.status_code == HTTPStatus.OK
        assert 'reason' in response.json()

    def test_numbers_in_values(self):
        """Негативный тест - в значениях передаются цифры."""
        response = requests.post(
            url=f'{self.BASE_URL}auth',
            headers={'Content-Type': 'application/json'},
            json={
                "username": "admin123",
                "password": "password123",
            },
        )

        assert response.status_code == HTTPStatus.OK
        assert 'reason' in response.json()

    def test_not_valid_content_type(self):
        """Негативный тест - в заоловке пердаётся не правильный Content-Type."""
        response = requests.post(
            url=f'{self.BASE_URL}auth',
            headers={'Content-Type': 'text/plain'},
            json={
                "username": "admin!@#$,.",
                "password": "!@#$,.password123",
            },
        )

        assert response.status_code == HTTPStatus.OK
        assert 'reason' in response.json()
