from methods.user_methods import UserMethods
from generators import Generatorss
import allure
from test_data import TestData as td

class TestChangeUserData:

    @allure.title("Изменить данные пользователя")
    def test_change_user_data(self, authorized_user):
        user_methods = UserMethods()
        body, token = authorized_user
        changed_body_data = body.copy()
        new_mail = Generatorss.generate_random_email()
        changed_body_data["email"] = new_mail
        changed_body_data["name"] = "new_name"
        user_data, status_code = user_methods.change_user_data(
            changed_body_data, token
        )

        assert (
            not isinstance(user_data, str)
            and user_data.get("user", {}).get("email") == new_mail
            and user_data.get("user", {}).get("name") == "new_name"
            and status_code == 200
        ), f"user_data:{user_data} and status_code: {status_code}"


        
    @allure.title("Нельзя изменить данные пользователя без авторизации")
    def test_change_user_data_without_autorisation(self, authorized_user):
        user_methods = UserMethods()
        body,_ = authorized_user
        changed_body_data = body.copy()
        new_mail = Generatorss.generate_random_email()
        changed_body_data["email"] = new_mail
        changed_body_data["name"] = "new_name"


        user_data, status_code = user_methods.change_user_data(
            changed_body_data, td.fake_token
        )

        assert (not isinstance (user_data, str)
                and user_data.get("success") == False
                and user_data.get("message") == 'You should be authorised'
                and status_code == 401 ),(
            f"user_data:{user_data} and status_code: {status_code}")
        
