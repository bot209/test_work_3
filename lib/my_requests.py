import requests
from lib.logger import Logger
import allure

class MyRequests:
    @staticmethod  
    def get(url: str, data: dict = None):
        with allure.step(f'GET запрос на сайт: {url}'):
            return MyRequests._send(url, data, 'GET')
    
    @staticmethod  
    def post(url: str, data: dict = None):
        with allure.step(f'POST запрос на сайт: {url}'):
            return MyRequests._send(url, data, 'POST')

    @staticmethod 
    def _send(url: str, data: dict, method: str):
        url = f'https://petstore.swagger.io/v2{url}'

        Logger.add_request(url, data, method)
        if method == 'GET':
            response = requests.get(url, params=data)
        elif method == 'POST':
            response = requests.post(url, data=data)
        else:
            raise Exception(f'Неверный HTTP метод: {method}')
        
        Logger.add_response(response)
        return response