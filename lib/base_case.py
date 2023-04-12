from requests import Response
import json.decoder

class BaseCase:
    def get_json(self, response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f'Ответ не в JSON. Ответ текста: "{response.text}"'

        assert name in response_as_dict, f'Ответ JSON не имеет ключа: "{name}"'
        return response_as_dict[name]