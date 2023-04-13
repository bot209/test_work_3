from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertion import Assertion
import pytest
import allure

@allure.epic('POST Methods')
@allure.suite('Update a pet')
@pytest.mark.POST_methods
class TestUpdatePet(BaseCase):
    def setup_method(self):
        self.petId = 5
        self.name = 'Test123'
        self.status = '123'
        self.data = {'petId': self.petId, 'name': self.name, 'status': self.status}
        
    @allure.title('Проверка статус кода, после изменения значений')
    @allure.description('Тест вернул правильный статус код, после изменения значений')
    def test_check_input_of_new_value(self):
        response1 = MyRequests.post(f'/pet/{self.petId}', data=self.data)
        Assertion.assert_code_status(response1, 200)
        
    @allure.title('Проверка изменения значений: petId, name, status')
    @allure.description('Тест вернул корректные значения: petId, name, status после их изменения')
    def test_check_changed_value(self):
        response2 = MyRequests.get(f'/pet/{self.petId}')
        Assertion.assert_code_status(response2, 200)
        Assertion.assert_json_value_by_name(response2, 'id', self.petId, 'Айдишник не сходятся')
        Assertion.assert_json_value_by_name(response2, 'name', self.name, 'Имена не сходятся')
        Assertion.assert_json_value_by_name(response2, 'status', self.status, 'Статусы не сходятся')

    @allure.title('Проверка ввода не корректных значений: petId, name, status')
    @allure.description('Тест вернул правильный статус код, после ввода некорректных значений: petId, name, status')
    def test_check_input_of_icorrect_value(self):
        petId = 'name'
        name = 123
        status = 123
        data = {'petId': petId, 'name': name, 'status': status}
        response = MyRequests.post(f'/pet/{petId}', data=data)
        Assertion.assert_code_status(response, 404)

    @allure.title('Проверка ввода пустых значений: petId, name, status')
    @allure.description('Тест вернул правильный статус код, после ввода пустых значений: petId, name, status')
    def test_check_for_empty_values(self):
        petId = ''
        name = ''
        status  = ''
        data = {'petId': petId, 'name': name, 'status': status}
        response = MyRequests.post(f'/pet/{petId}', data=data)
        Assertion.assert_code_status(response, 415)
