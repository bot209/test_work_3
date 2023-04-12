from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertion import Assertion
import requests

class TestUpdatePet(BaseCase):
    def setup_method(self):
        self.petId = 5
        self.name = 'test228'
        self.status = '123'
        self.data = {'petId': self.petId, 'name': self.name, 'status': self.status}
        
# 1. Изменить значения питомца
    def test_check_input_of_new_value(self):
        response1 = MyRequests.post(f'/pet/{self.petId}', data=self.data)
        Assertion.assert_code_status(response1, 200)
        
# 2. Проверить что данные изменились
    def test_check_changed_value(self):
        response2 = MyRequests.get(f'/pet/{self.petId}')
        Assertion.assert_json_value_by_name(response2, 'name', self.name, 'Имена не сходятся')
        Assertion.assert_json_value_by_name(response2, 'status', self.status, 'Статусы не сходятся')

# 3. Проверить ввод некорректных данных
    def test_check_input_of_icorrect_value(self):
        petId = 'name'
        name = 123
        status = 123
        data = {'petId': petId, 'name': name, 'status': status}
        response = MyRequests.post(f'/pet/{petId}', data=data)
        Assertion.assert_code_status(response, 404)

# 4. Проверить ввод пустых данных
    def test_check_for_empty_values(self):
        petId = ''
        name = ''
        status  = ''
        data = {'petId': petId, 'name': name, 'status': status}
        response = MyRequests.post(f'/pet/{petId}', data=data)
        Assertion.assert_code_status(response, 415)