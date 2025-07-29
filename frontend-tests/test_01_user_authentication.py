import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class TestUserAuthentication(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.base_url = "http://localhost:3000/login"  # Update if deployed

    def test_TC_01_LOGIN_valid_credentials(self):
        """
        TC-01-LOGIN: Validate user login with valid credentials
        """
        self.driver.get(self.base_url)
        time.sleep(1)

        self.driver.find_element(By.NAME, "email").send_keys("validuser@example.com")
        self.driver.find_element(By.NAME, "password").send_keys("ValidPassword123")
        self.driver.find_element(By.XPATH, "//button[text()='Login']").click()
        time.sleep(2)

        # Assert: redirected to dashboard
        self.assertIn("/dashboard", self.driver.current_url)

    def test_TC_01_LOGIN_invalid_credentials(self):
        """
        TC-01-LOGIN-INVALID: Validate login with invalid credentials
        """
        self.driver.get(self.base_url)
        time.sleep(1)

        self.driver.find_element(By.NAME, "email").send_keys("invalid@example.com")
        self.driver.find_element(By.NAME, "password").send_keys("WrongPass123")
        self.driver.find_element(By.XPATH, "//button[text()='Login']").click()
        time.sleep(2)

        # Assert: error message shown (adjust based on your implementation)
        error_elements = self.driver.find_elements(By.CLASS_NAME, "error-message")
        self.assertTrue(any("invalid" in e.text.lower() for e in error_elements))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
