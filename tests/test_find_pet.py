from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertion import Assertion

class TestFindPet(BaseCase):
    def setup_method(self):
        self.petId = 5
        response = MyRequests.get(f'/pet/{self.petId}')
        self.pet_id = self.get_json(response, 'id')
        self.pet_name = self.get_json(response, 'name')

# 1. Проверить получение правильного статус кода
    def test_get_valid_status_code(self):
        response = MyRequests.get(f'/pet/{self.petId}')
        Assertion.assert_code_status(response, 200)

# 2. Проверить что нам приходят значения id, name питомца
    def test_get_valid_pet_id_and_name(self):
        response = MyRequests.get(f'/pet/{self.petId}')
        Assertion.assert_json_has_key(response, 'id')
        Assertion.assert_json_has_key(response, 'name')  

# 3. Проверить ввод некорректного Id питомца
    def test_get_no_valid_pet_id(self):
        response = MyRequests.get('/pet/2222')
        Assertion.assert_code_status(response, 404)

# 4. Проверить ввод пустого значения id питомца
    def test_get_not_valid_params(self):
        response = MyRequests.get('/pet/')
        Assertion.assert_code_status(response, 405)


    