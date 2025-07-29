import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class TestCoordinatorDashboard(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = Options()
        options.add_argument("--start-maximized")
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.get("http://localhost:3000/login")  # Update this if your frontend is hosted elsewhere

        # Login as Coordinator
        cls.driver.find_element(By.NAME, "email").send_keys("coordinator@example.com")
        cls.driver.find_element(By.NAME, "password").send_keys("password123")
        cls.driver.find_element(By.XPATH, "//button[text()='Login']").click()
        time.sleep(2)

    def test_TC_02_COORDINATOR_VIEW(self):
        """
        TC-02-COORDINATOR-VIEW: Verify coordinator can view dashboard
        """
        self.assertIn("/dashboard", self.driver.current_url)
        header = self.driver.find_element(By.TAG_NAME, "h1").text.lower()
        self.assertIn("coordinator", header)

    def test_TC_02_CREATE_TASK(self):
        """
        TC-02-CREATE-TASK: Create a new task from dashboard
        """
        self.driver.find_element(By.ID, "create-task-button").click()
        time.sleep(1)
        self.driver.find_element(By.NAME, "title").send_keys("New Test Task")
        self.driver.find_element(By.NAME, "description").send_keys("This is a sample task")
        self.driver.find_element(By.XPATH, "//button[text()='Submit']").click()
        time.sleep(2)

        # Check that the new task appears in the task list
        tasks = self.driver.find_elements(By.CLASS_NAME, "task-title")
        self.assertTrue(any("New Test Task" in task.text for task in tasks))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
