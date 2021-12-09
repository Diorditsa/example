

class LoginPage():
    def __init__(self):
        pass

    log_in_button = {
        "selector": "//span[contains(.,'Войти')]",
        "type_selector": "by_xpath"
    }
    email_field = {
        "selector": "//input[@id='email']",
        "type_selector": "by_xpath"
    }
    password_field = {
        "selector": "//input[@id='pass']",
        "type_selector": "by_xpath"
    }
    entrance_next_button = {
        "selector": "//button[@id='btn-entrance']",
        "type_selector": "by_xpath"
    }


