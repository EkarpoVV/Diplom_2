import random
import string

class Generatorss:

    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string    
    
    def generate_random_email():
        email = f"user{random.randint(1000, 9999)}@test-example.com"
        return email

    def generate_random_payload_for_register_new_user(self):
        email = Generatorss.generate_random_email()
        password = Generatorss.generate_random_string(10)
        name = Generatorss.generate_random_string(10)

        payload = {
                "email": email,
                "password": password,
                "name": name
        }
        return payload    
       