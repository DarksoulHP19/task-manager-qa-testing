import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class TestUserProfile(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = Options()
        options.add_argument("--start-maximized")
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.get("http://localhost:3000/login")  # Update if needed

        # Login as any valid user
        cls.driver.find_element(By.NAME, "email").send_keys("user@example.com")
        cls.driver.find_element(By.NAME, "password").send_keys("password123")
        cls.driver.find_element(By.XPATH, "//button[text()='Login']").click()
        time.sleep(2)

        # Navigate to Profile
        cls.driver.find_element(By.ID, "user-avatar").click()
        time.sleep(1)
        cls.driver.find_element(By.LINK_TEXT, "Profile").click()
        time.sleep(2)

    def test_TC_08_VIEW_PROFILE(self):
        """
        TC-08-VIEW-PROFILE: View user profile
        """
        profile_header = self.driver.find_element(By.TAG_NAME, "h2").text.lower()
        self.assertIn("profile", profile_header)
        email_field = self.driver.find_element(By.ID, "user-email").text
        self.assertIn("@", email_field)

    def test_TC_08_EDIT_PROFILE(self):
        """
        TC-08-EDIT-PROFILE: Edit and update profile information
        """
        self.driver.find_element(By.ID, "edit-profile-button").click()
        time.sleep(1)
        name_input = self.driver.find_element(By.NAME, "name")
        name_input.clear()
        name_input.send_keys("Updated User")
        self.driver.find_element(By.XPATH, "//button[text()='Save Changes']").click()
        time.sleep(2)

        updated_name = self.driver.find_element(By.ID, "user-name").text
        self.assertIn("Updated User", updated_name)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
