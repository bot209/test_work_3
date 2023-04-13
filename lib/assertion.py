from requests import Response
import json
import allure

class Assertion:
    @staticmethod
    @allure.step('Проверка статус кода')
    def assert_code_status(response: Response, expected_status_code):
        assert response.status_code == expected_status_code, \
            f'Неожиданный статус код! Ожидаемый результат: {expected_status_code}. Фактический: {response.status_code}'
        
    @staticmethod
    @allure.step('Проверка наличия ключа в JSON')
    def assert_json_has_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f'Ответ не в JSON. Ответ текста: "{response.text}"'
        assert name in response_as_dict, f'В ответе JSON нет ключа: "{name}"'

    @staticmethod
    @allure.step('Проверка на содержания ключа в JSON')
    def assert_json_has_not_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f'Ответ не в JSON. Ответ текста: "{response.text}"'
        assert name not in response_as_dict, f'Ответ JSON не должен содержать {name}. Но он присутствует'

    @staticmethod
    @allure.step('Проверка наличия значения в ключе JSON')
    def assert_json_value_by_name(response: Response, name, expected_value, error_message):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f'Ответ не в JSON. Ответ текста: "{response.text}"'
        assert name in response_as_dict, f'Ответ JSON не имеет ключа: "{name}"'
        assert response_as_dict[name] == expected_value, error_message
