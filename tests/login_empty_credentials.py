import unittest
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginEmptyCredentialsTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        option = webdriver.FirefoxOptions()
        option.add_argument('--headless')
        cls.browser = webdriver.Firefox(options=option)

    def test_1_login_empty_credentials(self):
        login_url = 'http://localhost/login.php'
        response = requests.post(login_url, data={})
        
        self.assertIn('<form class="form-signin"', response.text)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2, warnings='ignore')
