import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class TestUserDashboard(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = Options()
        options.add_argument("--start-maximized")
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.get("http://localhost:3000/login")  # Update if hosted elsewhere

        # Login as a general user
        cls.driver.find_element(By.NAME, "email").send_keys("user@example.com")
        cls.driver.find_element(By.NAME, "password").send_keys("password123")
        cls.driver.find_element(By.XPATH, "//button[text()='Login']").click()
        time.sleep(2)

    def test_TC_05_USER_DASHBOARD_LOAD(self):
        """
        TC-05-USER-DATA: User can view and update dashboard widgets
        """
        self.assertIn("/dashboard", self.driver.current_url)
        dashboard = self.driver.find_element(By.ID, "user-dashboard")
        self.assertTrue(dashboard.is_displayed(), "User dashboard not visible")

    def test_TC_05_WIDGET_INTERACTION(self):
        """
        TC-05-WIDGET-INTERACTION: Interact with dashboard widget
        """
        widget = self.driver.find_element(By.CLASS_NAME, "dashboard-widget")
        widget.click()
        time.sleep(1)

        widget_modal = self.driver.find_element(By.ID, "widget-detail-modal")
        self.assertTrue(widget_modal.is_displayed(), "Widget detail modal did not appear")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
