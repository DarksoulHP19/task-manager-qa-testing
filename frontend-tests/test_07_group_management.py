import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class TestGroupManagement(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = Options()
        options.add_argument("--start-maximized")
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.get("http://localhost:3000/login")  # Update this if needed

        # Login as Coordinator or Admin
        cls.driver.find_element(By.NAME, "email").send_keys("coordinator@example.com")
        cls.driver.find_element(By.NAME, "password").send_keys("password123")
        cls.driver.find_element(By.XPATH, "//button[text()='Login']").click()
        time.sleep(2)

        # Navigate to Group Management
        cls.driver.find_element(By.LINK_TEXT, "Groups").click()
        time.sleep(1)

    def test_TC_07_CREATE_GROUP(self):
        """
        TC-07-CREATE-GROUP: Create a new group
        """
        self.driver.find_element(By.ID, "create-group-button").click()
        time.sleep(1)
        self.driver.find_element(By.NAME, "groupName").send_keys("Selenium Test Group")
        self.driver.find_element(By.XPATH, "//button[text()='Create']").click()
        time.sleep(2)

        group_names = self.driver.find_elements(By.CLASS_NAME, "group-name")
        self.assertTrue(any("Selenium Test Group" in g.text for g in group_names))

    def test_TC_07_ADD_MEMBER(self):
        """
        TC-07-ADD-MEMBER: Add a user to the group
        """
        # Click the first group's "Manage" or similar button
        self.driver.find_element(By.CLASS_NAME, "manage-group-button").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "add-member-button").click()
        time.sleep(1)
        self.driver.find_element(By.NAME, "userEmail").send_keys("intern@example.com")
        self.driver.find_element(By.XPATH, "//button[text()='Add']").click()
        time.sleep(2)

        members = self.driver.find_elements(By.CLASS_NAME, "member-email")
        self.assertTrue(any("intern@example.com" in m.text for m in members))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
