import allure
from methods.order_methods import OrderMethods
from test_data import TestData as td
import pytest


class TestCreateOrder:  

    @allure.title("Создание заказа с разными некорректными ингредиентами")
    @pytest.mark.parametrize(
        "ingredients, expected_status, expected_success",
        td.invalid_ingredients
    )
    def test_create_order_invalid_ingredients(
        self, authorized_user, ingredients, expected_status, expected_success
    ):
        _, token = authorized_user
        order_methods = OrderMethods()
        body = {"ingredients": ingredients}
        order_data, status_code = order_methods.create_order(body, token)

        assert (
            status_code == expected_status and
            (
                expected_success is None or
                (
                    not isinstance(order_data, str) and
                    order_data.get('success') is expected_success
                )
            )
        ), f"user_data:{order_data} and status_code: {status_code}"