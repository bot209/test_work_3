import datetime
import os
from requests import Response

class Logger:
    if not os.path.exists('test_logs'):
        os.makedirs('test_logs')
    file_name = f'test_logs/log_' + str(datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')) + '.log'

    @classmethod
    def _write_logs_to_file(cls, data: str):
        with open(cls.file_name, 'a', encoding='utf-8') as looger_file:
            looger_file.write(data)

    @classmethod
    def add_request(cls, url: str, data: dict, method: str):
        testname = os.environ.get('PYTEST_CURRENT_TEST')
        
        data_to_add = f'\n--------------------------------------------------------------------------------------------------------\n'
        data_to_add += f'Тест: {testname}\n'
        data_to_add += f'Время: {str(datetime.datetime.now())}\n'
        data_to_add += f'Метод запрос: {method}\n'
        data_to_add += f'URL запроса: {url}\n'
        data_to_add += f'Data запроса: {data}\n'
        data_to_add += '\n'
        cls._write_logs_to_file(data_to_add)

    @classmethod
    def add_response(cls, response: Response):
        data_to_add =f'Время: {str(datetime.datetime.now())}\n'
        data_to_add += f'Статус код ответа: {response.status_code}\n'
        data_to_add += f'Текст ответа: {response.text}\n'
        data_to_add += f'\n--------------------------------------------------------------------------------------------------------\n'
        cls._write_logs_to_file(data_to_add)