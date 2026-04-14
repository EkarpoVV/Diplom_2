import allure
from generators import Generatorss
import requests
from urls import *
import json

class UserMethods:
    @allure.step("Создать пользователя")
    def create_user(self, body = None):
        if body is None:
            body = Generatorss.generate_random_payload_for_register_new_user(self).copy()
        response = requests.post(
                f"{BASE_URL}{USER_URL}register", json=body)
        try:
            return response.json(), response.status_code, body  # body возвращать?
        except json.decoder.JSONDecodeError:
            return response.text, response.status_code, body # body возвращать?
            
    @allure.step("Логин пользователя")
    def login_user(self, body):
        response = requests.post(f"{BASE_URL}{USER_URL}login", json=body) 
        try:
            return response.json(), response.status_code # body возвращать?
        except json.decoder.JSONDecodeError:
            return response.text, response.status_code # body возвращать?


    @allure.step("Удалить пользователя")
    def delete_user(self, authorization):
        authorization_headers = {"Authorization": authorization}
        response = requests.delete(f'{BASE_URL}{USER_URL}user',headers=authorization_headers)
        try:
            return response.json(), response.status_code # body возвращать?
        except json.decoder.JSONDecodeError:
            return response.text, response.status_code
        
    @allure.step("Изменить данные пользователя")
    def change_user_data(self,new_body,authorization):
        authorization_headers = {"Authorization": authorization}
        response = requests.patch(f'{BASE_URL}{USER_URL}user',headers=authorization_headers, json=new_body)
        try:
            return response.json(), response.status_code
        except json.decoder.JSONDecodeError:
            return response.text, response.status_code
