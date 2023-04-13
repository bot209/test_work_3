import requests
import allure

class MyRequests:
    @staticmethod
    @allure.step('GET запрос')    
    def get(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        return MyRequests._send(url, data, headers, cookies, 'GET')
    
    @staticmethod
    @allure.step('POST запрос')    
    def post(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        return MyRequests._send(url, data, headers, cookies, 'POST')

    @staticmethod 
    def _send(url: str, data: dict, headers: dict, cookies: dict, method: str):
        url = f'https://petstore.swagger.io/v2{url}'

        if headers is None:
            headers = {}
        if cookies is None:
            cookies = {}
        
        if method == 'GET':
            response = requests.get(url, params=data, headers=headers, cookies=cookies)
        elif method == 'POST':
            response = requests.post(url, data=data, headers=headers, cookies=cookies)
        else:
            raise Exception(f'Неверный HTTP метод: {method}')
        return response
    