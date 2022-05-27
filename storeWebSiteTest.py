from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# configura o caminho para o chromedriver
PATH = Service('/home/degemar/chromedriver')
driver = webdriver.Chrome(service=PATH)

# acessa a página web
driver.get('https://www.saucedemo.com/')

# procura pelo campo do formulário para adicionar o nome do usuario
username = driver.find_element(By.ID, 'user-name')

# escreve o nome do usuario
username.send_keys('standard_user')

# procura pelo campo do formulário para adicionar a senha
password = driver.find_element(By.ID, 'password')

# escreve a senha
password.send_keys('secret_sauce')

# procura pelo botão de login e depois aciona o click
login_btn = driver.find_element(By.ID, 'login-button')
login_btn.click()

# espera aparecer a lista de produtos
try:
    inventory = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'inventory_container'))
    )
except:
    driver.quit()

time.sleep(2)

# procura pelo select drop down para filtrar os produtos pelo preço mais baixo ao mais caro
filter_drop_down = Select(driver.find_element(By.CLASS_NAME, 'product_sort_container'))
filter_drop_down.select_by_visible_text('Price (low to high)')

# procura pelo primeiro produto e clica no botão para adicionar ele ao carrinho
sauce_labs_onesie_btn = driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie')
sauce_labs_onesie_btn.click()

# procura pelo segundo produto e clica no botão para adicionar ele ao carrinho
t_shirt_red_btn = driver.find_element(By.ID, 'add-to-cart-test.allthethings()-t-shirt-(red)')
t_shirt_red_btn.click()

# procura pelo botão do carrinho e depois clica nele para acessar a lista de compras
shopping_cart_btn = driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
shopping_cart_btn.click()

# espera aparecer a lista de compras com os produtos devidamente adicionados
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

# procura pelo botão de chekout para finalizar a compra e depois clica nele
checkout_btn = driver.find_element(By.ID, 'checkout')
checkout_btn.click()

# espera o formulário e suas entradas renderizarem na página
try:
    form_info = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'checkout_info_container'))
    )
    first_name_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'first-name'))
    )
    last_name_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'last-name'))
    )
    post_code_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'postal-code'))
    )
except:
    driver.quit()

# encontra o campo do primeiro nome e insere o texto
first_name = driver.find_element(By.ID, 'first-name')
first_name.send_keys('standard')

# encontra o campo do último nome e insere o texto
last_name = driver.find_element(By.ID, 'last-name')
last_name.send_keys('user')

# encontra o campo do código postal e insere a informação
post_code = driver.find_element(By.ID, 'postal-code')
post_code.send_keys('11111-111')

# espera 5 segundos antes de sair do navegador
time.sleep(5)

driver.quit()
