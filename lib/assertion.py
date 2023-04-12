from requests import Response
import json

class Assertion:
    @staticmethod
    def assert_code_status(response: Response, expected_status_code):
        assert response.status_code == expected_status_code, \
            f'Неожиданный статус код! Ожидаемый результат: {expected_status_code}. Фактический: {response.status_code}'
        
    @staticmethod
    def assert_json_has_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f'Ответ не в JSON. Ответ текста: "{response.text}"'
        assert name in response_as_dict, f'В ответе JSON нет ключа: "{name}"'

    @staticmethod
    def assert_json_has_not_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f'Ответ не в JSON. Ответ текста: "{response.text}"'
        assert name not in response_as_dict, f'Ответ JSON не должен содержать {name}. Но он присутствует'
