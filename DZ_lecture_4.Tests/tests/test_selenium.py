import configparser
import time
import unittest

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class TestAuthYandex(unittest.TestCase):
    def setUp(self):
        self.user_login, self.user_password = self.get_auth_data()
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(
            options=options, service=Service("\\chromedriverwin32\\chromedriver.exe")
        )
        self.driver.maximize_window()

    @staticmethod
    def get_auth_data():
        config = configparser.ConfigParser()
        config.read("..\\settings.ini")
        user_login = config["Yandex"]["user"]
        user_password = config["Yandex"]["password"]
        assert user_login != ""
        assert user_password != ""
        return user_login, user_password

    def test_auth(self):
        self.driver.get("https://passport.yandex.ru/auth/")
        assert self.driver.current_url == "https://passport.yandex.ru/auth"
        input_login = self.driver.find_element(By.ID, "passp-field-login")
        input_login.send_keys(self.user_login)
        input_login.send_keys(Keys.RETURN)
        self.driver.implicitly_wait(10)
        input_password = self.driver.find_element(By.ID, "passp-field-passwd")
        input_password.send_keys(self.user_password)
        input_password.send_keys(Keys.RETURN)
        self.driver.implicitly_wait(10)
        time.sleep(5)
        assert self.driver.current_url == "https://id.yandex.ru/"

    def tearDown(self):
        time.sleep(5)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
