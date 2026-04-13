import allure
import requests
from urls import *
import json

class OrderMethods:

    @allure.step("Получить ингридиенты")
    def get_ingredients(self):
        response = requests.get(f"{BASE_URL}{INGREDIENTS}")
        try:
            return response.json(), response.status_code
        except json.decoder.JSONDecodeError:
            return response.text, response.status_code

    @allure.step("Создать заказ")
    def create_order(self,body, autorisation):
        autorisation = {"Authorization": autorisation}  
        response = requests.post(f"{BASE_URL}{ORDERS_URL}", headers = autorisation, json=body)
        try:
            return response.json(), response.status_code
        except json.decoder.JSONDecodeError:
            return response.text, response.status_code
    
    @allure.step("Получить заказы пользователя")
    def get_user_orders(self, token):
        token = {"Authorization": token} 
        response = requests.get(f"{BASE_URL}{ORDERS_URL}", headers = token)
        try:
            return response.json(), response.status_code
        except:
            return response.text, response.status_code