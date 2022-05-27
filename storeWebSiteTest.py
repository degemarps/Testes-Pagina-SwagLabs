from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

PATH = Service('/home/degemar/chromedriver')
driver = webdriver.Chrome(service=PATH)

driver.get('https://www.saucedemo.com/')

username = driver.find_element(By.ID, 'user-name')
username.send_keys('standard_user')

password = driver.find_element(By.ID, 'password')
password.send_keys('secret_sauce')

password.send_keys(Keys.RETURN)

try:
    inventory = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'inventory_container'))
    )
except:
    driver.quit()

filter_drop_down = Select(driver.find_element(By.CLASS_NAME, 'product_sort_container'))
filter_drop_down.select_by_visible_text('Price (low to high)')

time.sleep(5)

driver.quit()
