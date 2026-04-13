from methods.user_methods import UserMethods
import allure

class TestLoginUser:


    @allure.title("Пользователь может залогиниться")
    def test_login_user_positive(self, user):
        user_methods = UserMethods()
        user_data, status_code = user_methods.login_user(user[2]) ## может возвращать только боди и обойтись без индекса, дальше будет видно
        
        assert (not isinstance (user_data, str) and user_data.get('success') is True and status_code == 200 ),(
            f"user_data:{user_data} and status_code: {status_code}")

    #Я специально не использовал параметрицию в этом и следующем кейсе, чтобы создавать новых пользователей и на лету менять данные
    @allure.title("Пользователь не может залогиниться с невырным email") 
    def test_login_user_incorrect_email(self, user):
        user_methods = UserMethods()
        incorrect_email_body = user[2].copy()
        incorrect_email_body['email'] = 'incorrect@incorrect.com'
        user_data, status_code =  user_methods.login_user(incorrect_email_body)
        
        assert (not isinstance (user_data, str) and user_data.get('success') is False and status_code == 401 ),(
            f"user_data:{user_data} and status_code: {status_code}")
    
    @allure.title("Пользователь не может залогиниться с невырным password") 
    def test_login_user_incorrect_password(self, user):
        user_methods = UserMethods()
        incorrect_email_body = user[2].copy()
        incorrect_email_body['password'] = 'incorrect_password'
        user_data, status_code =  user_methods.login_user(incorrect_email_body)
        
        assert (not isinstance (user_data, str) and user_data.get('success') is False and status_code == 401 ),(
            f"user_data:{user_data} and status_code: {status_code}")
    



        
