import time
from bs4 import BeautifulSoup

class Tests():
    def __init__(self, driver, report_file) -> None:
        self.driver = driver
        self.report_file = report_file

    def clear_report_file(self):
        with open(self.report_file, 'w') as f:
            f.write("Test Report:\n")

    def log_test_result(self, test_case, status, error=None):
        current_time = time.strftime("%Y-%m-%d %H:%M:%S")
        with open(self.report_file, 'a') as f:
            f.write(f"\n\n{current_time} \nTEST CASE:  '{test_case}' \nTEST CASE STATUS:  {status}")
            if error:
                f.write(f" - {error}")
            f.write("\n")

    def run_login_test(self, email, password):
        try:
            self.log_test_result(f"Login Test: '{email} {password}'", "Running")
            self.driver.get("https://app.asana.com/-/login")
            email_input = self.driver.find_element('xpath', "//input[@type='text']")
            email_input.send_keys(str(email))
            time.sleep(1)
            self.driver.find_elements('xpath', "//div[@role='button']")[1].click()
            time.sleep(6)
            password_input = self.driver.find_element('xpath', "//input[@type='password']")
            password_input.send_keys(str(password))
            time.sleep(2)
            previous = self.driver.current_url.strip()
            login_button = self.driver.find_element('xpath',
                                                   "//div[@class='ThemeableRectangularButtonPresentation--isEnabled ThemeableRectangularButtonPresentation ThemeableRectangularButtonPresentation--large NuxButton LoginPasswordForm-loginButton']")
            login_button.click()
            time.sleep(5)
            curr = self.driver.current_url.strip()

            assert previous != curr, "Login test case failed"
            if previous != curr:

                self.log_test_result(f"Login Task: '{email} {password}'", "Passed")
            else:

                self.log_test_result(f"Login Task: '{email} {password}'", "Failed", "Invalid Data")

        except Exception as e:
            x = {str(e)}

            self.log_test_result(f"Login Task: '{email} {password}'", "Failed", str(e))

    def run_create_task(self, task):
        time.sleep(2)
        try:
            self.log_test_result(f"\Create Task: '{task}'", "Running")
            time.sleep(6)
            self.driver.find_elements('xpath', "//div[@role='button']")[2].click()
            time.sleep(4)
            self.driver.find_element('xpath',
                                     "//div[@class='LeftIconItemStructure--isHighlighted LeftIconItemStructure LeftIconItemStructure--alignCenter MenuItemA11y-content']").click()
            time.sleep(3)
            taskName = self.driver.find_element('xpath', "//input[@type='text']")

            if (task is not None):
                taskName.send_keys(task)
                time.sleep(2)
                self.driver.find_element('xpath',
                                         "//div[@class='ThemeableRectangularButtonPresentation--isEnabled ThemeableRectangularButtonPresentation ThemeableRectangularButtonPresentation--large PrimaryButton--standardTheme PrimaryButton QuickAddTaskToolbar-createButton']").click()
                time.sleep(3)
                self.log_test_result(f"Create Task: '{task}'", "Passed")
            else:
                self.log_test_result(f"Create Task: '{task}'", "Failed","Null Values not accepted")


        except Exception as e:
            x = {str(e)}
            self.log_test_result(f"Create Task: '{task}'", "Failed", str(e))

    def run_check_task(self, task):
        try:
            self.log_test_result(f"Check Task: '{task}'", "Running")
            time.sleep(2)
            self.driver.get("https://app.asana.com")

            time.sleep(8)
            self.driver.find_element('xpath',
                                     "//div[@class='MyTasksWidgetContent-titleAndTabs']").click()
            time.sleep(5)
            html_content = self.driver.page_source
            soup = BeautifulSoup(html_content, 'html.parser')
            all_data = soup.find_all(string=True)
            found = False
            for data in all_data:
                if data == task:
                    found = True
                    self.log_test_result(f"Check Task: '{task}'", "Passed")
                    break
            if found==False:
                self.log_test_result(f"Check Task: '{task}'", "Failed", "Task not found")

        except Exception as e:
            x = {str(e)}
            self.log_test_result(f"Check Task: '{task}'", "Failed", str(e))


    def run_create_project(self, name):
        try:
            self.log_test_result(f"\n\nCreate Project Task: '{name}'", "Running")
            time.sleep(2)
            if (name is not None):
                self.driver.get("https://app.asana.com/0/projects/new")
                time.sleep(6)
                self.driver.find_element('xpath',
                                         "//div[@class='TileStructure TileStructure--sizeNormal FlowPickerTile']").click()
                time.sleep(5)
                project = self.driver.find_element('xpath', "//input[@type='text']")
                project.send_keys(name)
                time.sleep(2)
                self.driver.find_element('xpath',
                                         "//div[@class='ThemeableRectangularButtonPresentation--isEnabled ThemeableRectangularButtonPresentation ThemeableRectangularButtonPresentation--large PrimaryButton--standardTheme PrimaryButton BlankProjectDetailsForm-submitButton']").click()

                time.sleep(6)

                checkText = self.driver.find_element('xpath', "//input[@type='text']").get_attribute('value')
                assert checkText == name, "Test Check Failed"
                if (checkText == name):
                    self.log_test_result(f"Create Project Test: '{name}'", "Passed")
            else:
                self.log_test_result(f"Create Project Test: '{name}'","Failed", "None Value")
        except Exception as e:
            x = {str(e)}
            self.log_test_result(f"Create Project Test: '{name}'","Failed", str(e))


    def run_delete_task(self):
        time.sleep(2)
        try:
            self.log_test_result("Delete Task", "Running")

            self.driver.get("https://app.asana.com/0/1205789568375732/list")
            time.sleep(11)
            self.driver.find_element('xpath',
                                     "//div[@class='SpreadsheetGridTaskNameAndDetailsCellGroup-detailsButtonClickArea']").click()
            time.sleep(4)
            self.driver.find_element('xpath', "//div[@aria-label='More actions for this task']").click()
            time.sleep(3)
            taskName = self.driver.find_elements('xpath', "//div[@class='ExtraActionsMenuItemLabel']")[6].click()
            time.sleep(3)
            self.log_test_result(f"Delete Task", "Passed")

        except Exception as e:
            self.log_test_result(f"Delete Task", "Failed", str(e))
