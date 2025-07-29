import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class TestInternDashboard(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = Options()
        options.add_argument("--start-maximized")
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.get("http://localhost:3000/login")  # Update if hosted elsewhere

        # Login as Intern
        cls.driver.find_element(By.NAME, "email").send_keys("intern@example.com")
        cls.driver.find_element(By.NAME, "password").send_keys("password123")
        cls.driver.find_element(By.XPATH, "//button[text()='Login']").click()
        time.sleep(2)

    def test_TC_04_INTERN_VIEW_DASHBOARD(self):
        """
        TC-04-INTERN-VIEW: Intern sees dashboard
        """
        self.assertIn("/dashboard", self.driver.current_url)
        heading = self.driver.find_element(By.TAG_NAME, "h1").text.lower()
        self.assertIn("intern", heading)

    def test_TC_04_INTERN_ASSIGNED_TASKS(self):
        """
        TC-04-INTERN-ASSIGNED-TASKS: Assigned tasks are visible
        """
        task_list = self.driver.find_elements(By.CLASS_NAME, "task-card")
        self.assertGreater(len(task_list), 0, "Intern has no visible assigned tasks")

    def test_TC_04_INTERN_TASK_DETAILS(self):
        """
        TC-04-INTERN-TASK-DETAILS: Clicking on a task shows its details
        """
        self.driver.find_element(By.CLASS_NAME, "task-card").click()
        time.sleep(1)
        detail_view = self.driver.find_element(By.ID, "task-details")
        self.assertTrue(detail_view.is_displayed(), "Task details not displayed on click")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
