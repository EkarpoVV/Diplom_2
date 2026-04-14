import allure
from methods.order_methods import OrderMethods
from test_data import TestData as td
import pytest

class TestGetUserOrders:
    
    @allure.title("Получение заказов пользователя c авторизацией и без авторизации")
    @pytest.mark.parametrize(
        "token_type, expected_status, expected_success",
        [
            ("valid", 200, True),
            ("invalid", 401, False),
        ]
    )

    def test_get_user_orders_parametrize(self, token_type, expected_status, expected_success, user_with_orders):
        order_methods = OrderMethods()
        _, _, valid_token = user_with_orders
        token = valid_token if token_type == "valid" else td.fake_token
        orders_data, status_code = order_methods.get_user_orders(token)

        assert (
            not isinstance(orders_data, str)
            and status_code == expected_status
            and (
                (expected_success and orders_data.get("success") is True and orders_data.get("orders"))
                or
                (not expected_success and orders_data.get("success") is False)
            )
        ), f"user_data:{orders_data} and status_code: {status_code}"