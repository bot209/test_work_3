from requests import Response
import json.decoder
from datetime import datetime as dt

class BaseCase:
    def get_json(self, response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f'Ответ не в JSON. Ответ текста: "{response.text}"'

        assert name in response_as_dict, f'Ответ JSON не имеет ключа: "{name}"'
        return response_as_dict[name]
    
    def prepare_registration_data(self, email=None):
        if email is None:
            base_part = 'test'
            domain = 'test.io'
            random_part = dt.now().strftime('%m%d%Y%H%M%S')
            email = f'{base_part}{random_part}@{domain}'
        return {
            
        }