from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertion import Assertion
import pytest
import allure

@allure.epic('GET Methods')
@allure.suite('Find pet')
@pytest.mark.GET_methods
class TestFindPet(BaseCase):
    def setup_method(self):
        self.petId = 5
        response = MyRequests.get(f'/pet/{self.petId}')
        self.pet_id = self.get_json(response, 'id')
        self.pet_name = self.get_json(response, 'name')

    @allure.title('Проверка правильного статус кода')
    @allure.description('Тест успешно вернул статус код')
    def test_get_valid_status_code(self):
        response = MyRequests.get(f'/pet/{self.petId}')
        Assertion.assert_code_status(response, 200)

    @allure.title('Проверка корректности возврата значений: id, name')
    @allure.description('Тест успешно вернул значения: id, name')
    def test_get_valid_pet_id_and_name(self):
        response = MyRequests.get(f'/pet/{self.petId}')
        Assertion.assert_json_has_key(response, 'id')
        Assertion.assert_json_has_key(response, 'name')  

    @allure.title('Проверка некорректного значения: petId')
    @allure.description('Тест вернул правильный статус код, при проверке с некорректными значениями')
    def test_get_no_valid_pet_id(self):
        response = MyRequests.get('/pet/2222')
        Assertion.assert_code_status(response, 404)

    @allure.title('Проверка пустого запроса без эндопинта: /petId')
    @allure.description('Тест вернул правильный статус код, при проверке запроса с пустый эндпоинта')
    def test_get_not_valid_params(self):
        response = MyRequests.get('/pet/')
        Assertion.assert_code_status(response, 405)
