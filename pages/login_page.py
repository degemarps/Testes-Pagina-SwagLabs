from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import unittest
from testBase.webDriverSetup import WebDriverSetup


# testes da página de login
class Login_Page(WebDriverSetup):
    def test_login(self):
        # configura o caminho para o chromedriver
        PATH = Service('/home/degemar/chromedriver')
        self.driver = webdriver.Chrome(service=PATH)

        # acessa a página web
        self.driver.get('https://www.saucedemo.com/')

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


if __name__ == '__main__':
    unittest.main()