
import unittest
import time
from Tests import Tests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("https://app.asana.com/-/login")
        report_file = "test_report.log"
        cls.test = Tests(cls.driver, report_file)
        cls.test.clear_report_file()

    def test_1_successful_login(self):
        self.test.run_login_test("advkn", "roo34")
        time.sleep(3)
        self.test.run_login_test("ayansameer60@gmail.com", "root1234")

    def test_2_create_task(self):
        self.test.run_create_task("Coding")
        time.sleep(3)
        self.test.run_create_task(None)

    def test_3_check_task(self):
        self.test.run_check_task("Coding")
        time.sleep(3)
        self.test.run_check_task("ZCACW")

    def test_4_create_project(self):
        self.test.run_create_project("TogoRide")
        time.sleep(3)
        self.test.run_create_project(None)

    def test_5_delete_task(self):
        self.test.run_delete_task()

    @classmethod
    def tearDownClass(cls):
        print("\nQuitting")
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()