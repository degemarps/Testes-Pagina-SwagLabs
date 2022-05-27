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

time.sleep(2)

filter_drop_down = Select(driver.find_element(By.CLASS_NAME, 'product_sort_container'))
filter_drop_down.select_by_visible_text('Price (low to high)')

sauce_labs_onesie_btn = driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie')
sauce_labs_onesie_btn.click()

t_shirt_red_btn = driver.find_element(By.ID, 'add-to-cart-test.allthethings()-t-shirt-(red)')
t_shirt_red_btn.click()

shopping_cart_btn = driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
shopping_cart_btn.click()

try:
    cart_list = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'cart_list'))
    )
    sauce_labs_onesie_item = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Sauce Labs Onesie'))
    )
    t_shirt_red_item = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Test.allTheThings() T-Shirt (Red)'))
    )
except:
    driver.quit()

time.sleep(5)

driver.quit()
