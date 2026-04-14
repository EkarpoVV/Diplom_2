

class TestData:

    registred_mandatory_filds = [
    {
    "password": "qlkajfxwhd", 
    "name": "thiyibfarb"
    },
    {
    "email": "user66417@test-example.com", 
    "name": "thiyibfarb"
    },        
    {
    "email": "user66417@test-example.com", 
    "password": "qlkajfxwhd"
    }
    ]

    incorrect_password_or_email  = [
          {
    "email": "incorrect@incorrect.com", 
    "password": "qlkajfxwhd"
    },
      {
    "email": "user66417@test-example.com", 
    "password": "qlkajfxwhd"
    },

    ]

    fake_token = "fake_token"

    invalid_ingredients =         [
            ([], 400, False),
            (["fake_ingredient_1", "fake_ingredient_2"], 500, None),
        ]