#explicit waits

from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager


class explicitWaits:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Firefox(service= Service(GeckoDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 10)

    def boot(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def findElementByXPATH(self, xpath):
        return self.driver.find_element(by=By.XPATH, value=xpath)



    def quit(self):
        self.driver.quit()

    def imbd(self):
        self.boot()
        try:
          self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/section/div/div[1]/div[1]/label/span[1]/div").click()))
          self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/section/div/div[2]/div[1]/label/span[1]/div").click()))
          print('successful')
        except NoSuchElementException as e:
            print(e)
        finally:
            self.quit()


if __name__ == "__main__":
    url = "https://www.imdb.com/search/name/"
    obj = explicitWaits








