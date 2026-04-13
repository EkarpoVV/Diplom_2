
import pytest
from methods.user_methods import UserMethods
from methods.order_methods import OrderMethods

@pytest.fixture()
def user():
    user_methods = UserMethods()
    user_data, status_code, body = user_methods.create_user()
    yield user_data, status_code, body
    user_methods.delete_user(user_data.get("accessToken"))

@pytest.fixture()
def authorized_user(user):
    user_methods = UserMethods()
    login_data, _ = user_methods.login_user(user[2])
    token = login_data["accessToken"]

    yield user[2], token

@pytest.fixture()
def user_with_orders(authorized_user):
    body, token = authorized_user
    order_methods = OrderMethods()
    list_ingredients,_ = order_methods.get_ingredients()
    if list_ingredients.get("data"):
        ingredient_1_id = list_ingredients["data"][0].get("_id")
        ingredient_2_id = list_ingredients["data"][1].get("_id")
    body = {"ingredients": [ingredient_1_id,ingredient_2_id]}
    order_data, status_code = order_methods.create_order(body, token)
   
    yield order_data, status_code, token