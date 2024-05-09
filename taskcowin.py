import time

import self
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.get('https://www.cowin.gov.in/')
driver.find_element(by=By.XPATH, value='//*[@id="navbar"]/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[4]/a').click()
driver.switch_to.window(driver.window_handles[1])
driver.maximize_window()
time.sleep(5)
driver.find_element(by=By.XPATH, value='//*[@id="navbar"]/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[5]/a').click()
driver.switch_to.window(driver.window_handles[2])
driver.maximize_window()
time.sleep(5)


driver.switch_to.window(driver.window_handles[2])
driver.quit()
driver.switch_to.window(driver.window_handles[1])
driver.quit()



