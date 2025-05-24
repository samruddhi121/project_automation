from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EmployeePage:

    def __init__(self, browser):

        self.browser = browser
        self.wait = WebDriverWait(browser, 10)

    # Locators
    CREATE_EMPLOYEE_BUTTON = (By.XPATH, "//a[@href='/employeemaster/CreateEmployee']")
    SELECT_CENTRE = (By.ID, "SelectedCentreCode")
    TITLE = (By.XPATH, "//select[@id='PersonTitle']")
    FIRST_NAME = (By.ID, "FirstName")
    LAST_NAME = (By.ID, "LastName")
    GENDER = (By.XPATH, "//select[@id='GenderEnumId']")
    EMAIL =(By.XPATH,"//input[@id='EmailId']")
    CALLINGCODE =(By.XPATH,"//select[@id='CallingCode']")
    MOBILE_NUMBER = (By.ID, "MobileNumber")
    SAVE_BUTTON = (By.CSS_SELECTOR, ".btn.btn-success")


    # Methods
    def click_create_employee_button(self):
        self.browser.find_element(*self.CREATE_EMPLOYEE_BUTTON).click()

    def fill_create_employee_form(self, first_name, last_name,gender,email, mobile, centre_name, title,callingcode):
        self.wait.until(EC.presence_of_element_located(self.SELECT_CENTRE))
        Select(self.browser.find_element(*self.SELECT_CENTRE)).select_by_visible_text(centre_name)
        Select(self.browser.find_element(*self.TITLE)).select_by_visible_text(title)
        self.browser.find_element(*self.FIRST_NAME).send_keys(first_name)
        self.browser.find_element(*self.LAST_NAME).send_keys(last_name)
        Select(self.browser.find_element(*self.GENDER)).select_by_visible_text(gender)
        self.browser.find_element(*self.EMAIL).send_keys(email)
        Select(self.browser.find_element(*self.CALLINGCODE)).select_by_visible_text(callingcode)
        self.browser.find_element(*self.MOBILE_NUMBER).send_keys(mobile)
        self.browser.find_element(*self.SAVE_BUTTON).click()


