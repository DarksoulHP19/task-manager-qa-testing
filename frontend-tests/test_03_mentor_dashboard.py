import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class TestMentorDashboard(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = Options()
        options.add_argument("--start-maximized")
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.get("http://localhost:3000/login")  # Update to your deployment if needed

        # Login as Mentor
        cls.driver.find_element(By.NAME, "email").send_keys("mentor@example.com")
        cls.driver.find_element(By.NAME, "password").send_keys("password123")
        cls.driver.find_element(By.XPATH, "//button[text()='Login']").click()
        time.sleep(2)

    def test_TC_03_MENTOR_VIEW(self):
        """
        TC-03-MENTOR-VIEW: Mentor sees assigned interns/tasks
        """
        self.assertIn("/dashboard", self.driver.current_url)
        heading = self.driver.find_element(By.TAG_NAME, "h1").text.lower()
        self.assertIn("mentor", heading)

    def test_TC_03_MENTOR_VIEW_ASSIGNED_TASKS(self):
        """
        TC-03-MENTOR-VIEW-ASSIGNED-TASKS: Check assigned tasks list appears
        """
        tasks_section = self.driver.find_element(By.ID, "assigned-tasks")
        tasks = tasks_section.find_elements(By.CLASS_NAME, "task-item")
        self.assertGreater(len(tasks), 0, "No tasks assigned to mentor")

    def test_TC_03_MENTOR_VIEW_INTERNS(self):
        """
        TC-03-MENTOR-VIEW-INTERNS: Check interns list is displayed
        """
        interns_section = self.driver.find_element(By.ID, "interns-list")
        interns = interns_section.find_elements(By.CLASS_NAME, "intern-card")
        self.assertGreater(len(interns), 0, "No interns assigned to mentor")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
