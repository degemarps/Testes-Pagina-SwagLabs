from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "/home/degemar/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://www.saucedemo.com/")

username = driver.find_element_by_id("user-name")
username.send_keys("standard_user")

password = driver.find_element_by_id("password")
password.send_keys("secret_sauce")

password.send_keys(Keys.RETURN)

try:
    inventory = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "inventory_container"))
    )
except:
    driver.quit()

time.sleep(5)

driver.quit()
