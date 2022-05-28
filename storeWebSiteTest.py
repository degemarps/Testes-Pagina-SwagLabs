from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import unittest


class SwagLabsPage(unittest.TestCase):

    def setUp(self):
        # configura o caminho para o chromedriver
        PATH = Service('/home/degemar/chromedriver')
        self.driver = webdriver.Chrome(service=PATH)

        # acessa a página web
        self.driver.get('https://www.saucedemo.com/')

    def test_login(self):
        # procura pelo campo do formulário para adicionar o nome do usuario
        username = self.driver.find_element(By.ID, 'user-name')

        # escreve o nome do usuario
        username.send_keys('standard_user')

        time.sleep(1)

        # procura pelo campo do formulário para adicionar a senha
        password = self.driver.find_element(By.ID, 'password')

        # escreve a senha
        password.send_keys('secret_sauce')

        time.sleep(1)

        # procura pelo botão de login e depois aciona o click
        login_btn = self.driver.find_element(By.ID, 'login-button')
        login_btn.click()

        # espera aparecer a lista de produtos
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, 'inventory_container'))
            )
        except:
            self.driver.quit()

        time.sleep(2)

    # def sort_and_add_products_to_cart(self):
    #     # procura pelo select drop down para filtrar os produtos pelo preço mais baixo ao mais caro
    #     filter_drop_down = Select(self.driver.find_element(By.CLASS_NAME, 'product_sort_container'))
    #     filter_drop_down.select_by_visible_text('Price (low to high)')
    #
    #     time.sleep(1)
    #
    #     # procura pelo primeiro produto e clica no botão para adicionar ele ao carrinho
    #     sauce_labs_onesie_btn = self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie')
    #     sauce_labs_onesie_btn.click()
    #
    #     time.sleep(1)
    #
    #     # procura pelo segundo produto e clica no botão para adicionar ele ao carrinho
    #     t_shirt_red_btn = self.driver.find_element(By.ID, 'add-to-cart-test.allthethings()-t-shirt-(red)')
    #     t_shirt_red_btn.click()
    #
    #     time.sleep(1)
    #
    #     # procura pelo botão do carrinho e depois clica nele para acessar a lista de compras
    #     shopping_cart_btn = self.driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
    #     shopping_cart_btn.click()
    #
    #     # espera aparecer a lista de compras com os produtos devidamente adicionados
    #     try:
    #         cart_list = WebDriverWait(self.driver, 10).until(
    #             EC.presence_of_element_located((By.CLASS_NAME, 'cart_list'))
    #         )
    #         sauce_labs_onesie_item = WebDriverWait(self.driver, 10).until(
    #             EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Sauce Labs Onesie'))
    #         )
    #         t_shirt_red_item = WebDriverWait(self.driver, 10).until(
    #             EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Test.allTheThings() T-Shirt (Red)'))
    #         )
    #     except:
    #         self.driver.quit()
    #
    #     time.sleep(2)
    #
    # def make_checkout(self):
    #     # procura pelo botão de chekout para finalizar a compra e depois clica nele
    #     checkout_btn = self.driver.find_element(By.ID, 'checkout')
    #     checkout_btn.click()
    #
    #     # espera o formulário e suas entradas renderizarem na página
    #     try:
    #         form_info = WebDriverWait(self.driver, 10).until(
    #             EC.presence_of_element_located((By.ID, 'checkout_info_container'))
    #         )
    #         first_name_input = WebDriverWait(self.driver, 10).until(
    #             EC.presence_of_element_located((By.ID, 'first-name'))
    #         )
    #         last_name_input = WebDriverWait(self.driver, 10).until(
    #             EC.presence_of_element_located((By.ID, 'last-name'))
    #         )
    #         post_code_input = WebDriverWait(self.driver, 10).until(
    #             EC.presence_of_element_located((By.ID, 'postal-code'))
    #         )
    #     except:
    #         self.driver.quit()
    #
    #     time.sleep(2)
    #
    # def write_data_for_checkout(self):
    #     # encontra o campo do primeiro nome e insere o texto
    #     first_name = self.driver.find_element(By.ID, 'first-name')
    #     first_name.send_keys('standard')
    #
    #     time.sleep(1)
    #
    #     # encontra o campo do último nome e insere o texto
    #     last_name = self.driver.find_element(By.ID, 'last-name')
    #     last_name.send_keys('user')
    #
    #     time.sleep(1)
    #
    #     # encontra o campo do código postal e insere a informação
    #     post_code = self.driver.find_element(By.ID, 'postal-code')
    #     post_code.send_keys('11111-111')
    #
    #     time.sleep(1)
    #
    #     # procura pelo botão de continue e depois aciona o click nele
    #     continue_btn = self.driver.find_element(By.ID, 'continue')
    #     continue_btn.click()
    #
    #     # espera aparecer a lista dos produtos adicionados e o resumo da compra
    #     try:
    #         cart_list = WebDriverWait(self.driver, 10).until(
    #             EC.presence_of_element_located((By.CLASS_NAME, 'cart_list'))
    #         )
    #         summary_info = WebDriverWait(self.driver, 10).until(
    #             EC.presence_of_element_located((By.CLASS_NAME, 'summary_info'))
    #         )
    #     except:
    #         self.driver.quit()
    #
    #     time.sleep(2)
    #
    # def final_page_for_checkout(self):
    #     # procura pelo botão de finish para concluir a compra e aciona o seu click
    #     finish_btn = self.driver.find_element(By.ID, 'finish')
    #     finish_btn.click()
    #
    #     # espera renderizar a tela de checkout completo
    #     try:
    #         checkout_container = WebDriverWait(self.driver, 10).until(
    #             EC.presence_of_element_located((By.ID, 'checkout_complete_container'))
    #         )
    #     except:
    #         self.driver.quit()
    #
    #     # procura pelo texto que confirma a finalização da compra na página
    #     self.driver.find_element(By.XPATH, '//h2[text()="THANK YOU FOR YOUR ORDER"]')
    #
    #     # espera 5 segundos antes de sair do navegador
    #     time.sleep(5)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
