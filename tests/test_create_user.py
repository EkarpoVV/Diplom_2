import allure
from methods.user_methods import UserMethods
from generators import Generatorss
import pytest
from test_data import TestData

class TestCrreateUser:

    @allure.title("Создать пользователя")
    def test_create_user(self):
        user_data, status_code,_ = UserMethods.create_user(self)
        assert (not isinstance (user_data, str) and user_data.get('success') is True and status_code == 200 ),(
            f"user_data:{user_data} and status_code: {status_code}")

    @allure.title("Нельзя создать пользователя c таким же email")
    def test_create_user_same_email(self):
        body = Generatorss.generate_random_payload_for_register_new_user(self)
        UserMethods.create_user(self, body)
        user_data, status_code,_ = UserMethods.create_user(self, body)
        assert (not isinstance (user_data, str) and user_data.get('success') is False  and status_code == 403 ),(
            f"user_data:{user_data} and status_code: {status_code}")

    @allure.title("Нельзя создать пользователя без обязательных полей")
    @pytest.mark.parametrize('body', TestData.registred_mandatory_filds)
    def test_create_user_mandatory_fields(self, body):
        user_data, status_code,_ = UserMethods.create_user(self, body)
        assert (not isinstance (user_data, str) and user_data.get('success') is False and status_code == 403 ),(
            f"user_data:{user_data} and status_code: {status_code}")