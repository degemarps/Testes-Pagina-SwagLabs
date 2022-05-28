import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import urllib3


# implementação dos métodos setup e teardown do selenium
class WebDriverSetup(unittest.TestCase):
    def setUp(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        # configura o caminho para o chromedriver
        PATH = Service('/home/degemar/chromedriver')
        self.driver = webdriver.Chrome(service=PATH)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        if (self.driver != None):
            print("Cleanup of test environment")
            self.driver.close()
            self.driver.quit()
