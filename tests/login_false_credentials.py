import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginFalseCredentialsTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        option = webdriver.FirefoxOptions()
        option.add_argument('--headless')
        cls.browser = webdriver.Firefox(options=option)

    def test_1_login_false_credentials(self):
        login_url = 'http://localhost/login.php'
        self.browser.get(login_url)

        self.browser.find_element(By.ID, 'inputUsername').send_keys('admin')
        self.browser.find_element(By.ID, 'inputPassword').send_keys('admin')
        self.browser.find_element(By.TAG_NAME, 'button').click()

    def test_2_login_page(self):           
        expected_result = "Wrong usename or password"
        
        actual_result = self.browser.find_element(By.CLASS_NAME, 'checkbox').text
        self.assertIn(expected_result, actual_result)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2, warnings='ignore')
