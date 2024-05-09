from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver import ActionChains

class DragAndDrop:


    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.action = ActionChains(self.driver)

    def boot(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.wait(5)

    def wait(self, secs):
        sleep(secs)

    def quit(self):
        self.driver.quit()



    def findElementByXpath(self, xpath):
        return self.driver.find_element(by=By.XPATH, value=xpath)

    def dragAndDrop(self):
        try:
            self.boot()
            self.wait(5)
            source = self.findElementByXpath('//*[@id="draggable"]')
            destination = self.findElementByXpath("//div[@id='droppable']")

            self.action.drag_and_drop(source, destination).perform()
            self.wait(3)


            text = self.findElementByXpath('//p[normalize-space()=Drag me to my target]').text
            if text == 'Dropped!':
                print('success : we dragged the element and dropped in it place')

            else:
                print('error')

        except NoSuchElementException as e:
            print(e)

        finally:
            self.wait(5)
            self.quit()


url = 'https://jqueryui.com/droppable/'
obj = DragAndDrop(url)
obj.dragAndDrop()
