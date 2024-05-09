import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.by import By


class SauceDemoAutomation:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def navigate_to_url(self, url):
        self.driver.get(url)

    def print_cookies(self):
        cookies = self.driver.get_cookies()
        print("Cookies:")
        for cookie in cookies:
            print(cookie)

    def login(self, username, password):
        username_input = self.driver.find_element(by=By.ID, value='user-name')
        password_input = self.driver.find_element(by=By.ID, value='password')
        login_button = self.driver.find_element(by=By.ID, value='login-button')
        time.sleep(10)

        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button.click()
        time.sleep(5)

        # Wait for login to complete and verify dashboard title


    def logout(self):
        menu_button = self.driver.find_element(by=By.ID, value="react-burger-menu-btn")
        menu_button.click()
        logout_button = self.driver.find_element(by=By.ID, value="logout_sidebar_link")
        logout_button.click()
        time.sleep(5)

        # Verify logout


    def run(self):
        self.navigate_to_url("https://www.saucedemo.com/")

        print("Before login:")
        self.print_cookies()

        self.login("standard_user", "secret_sauce")

        print("After login:")
        self.print_cookies()

        self.logout()

        print("After logout:")
        self.print_cookies()

        self.driver.quit()

if __name__ == "__main__":
    automation = SauceDemoAutomation()
    automation.run()
