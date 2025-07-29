import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class TestTaskManagement(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = Options()
        options.add_argument("--start-maximized")
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.get("http://localhost:3000/login")  # Update if needed

        # Login as Coordinator (or role that can manage tasks)
        cls.driver.find_element(By.NAME, "email").send_keys("coordinator@example.com")
        cls.driver.find_element(By.NAME, "password").send_keys("password123")
        cls.driver.find_element(By.XPATH, "//button[text()='Login']").click()
        time.sleep(2)

    def test_TC_06_CREATE_TASK(self):
        """
        TC-06-CREATE: Create a new task
        """
        self.driver.find_element(By.ID, "create-task-button").click()
        time.sleep(1)
        self.driver.find_element(By.NAME, "title").send_keys("Automated Task")
        self.driver.find_element(By.NAME, "description").send_keys("Created by Selenium script")
        self.driver.find_element(By.XPATH, "//button[text()='Submit']").click()
        time.sleep(2)

        task_titles = self.driver.find_elements(By.CLASS_NAME, "task-title")
        self.assertTrue(any("Automated Task" in task.text for task in task_titles))

    def test_TC_06_UPDATE_TASK(self):
        """
        TC-06-UPDATE: Update an existing task
        """
        # Assuming first task can be edited
        self.driver.find_element(By.CLASS_NAME, "edit-task-button").click()
        time.sleep(1)
        title_input = self.driver.find_element(By.NAME, "title")
        title_input.clear()
        title_input.send_keys("Updated Task Title")
        self.driver.find_element(By.XPATH, "//button[text()='Save']").click()
        time.sleep(2)

        task_titles = self.driver.find_elements(By.CLASS_NAME, "task-title")
        self.assertTrue(any("Updated Task Title" in task.text for task in task_titles))

    def test_TC_06_DELETE_TASK(self):
        """
        TC-06-DELETE: Delete an existing task
        """
        self.driver.find_element(By.CLASS_NAME, "delete-task-button").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[text()='Confirm']").click()
        time.sleep(2)

        task_titles = self.driver.find_elements(By.CLASS_NAME, "task-title")
        self.assertFalse(any("Updated Task Title" in task.text for task in task_titles))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
