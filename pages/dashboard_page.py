from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    URL = "http://coditech-stage-admin.coditech.co.in/dashboard/index"

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)

    # Locators
    DASHBOARD = (By.XPATH, "//div[@class='page-content']")
    USERMENU_BUTTON = (By.CSS_SELECTOR, "a[role='button']")
    LOGOUT_BUTTON = (By.XPATH, "//a[normalize-space()='Logout']")
    EMPLOYEE_BUTTON = (By.XPATH, "//a[@href='/employeemaster/list']//div[@class='card report-card']//div[@class='card-body']")
    CREATE_EMPLOYEE =(By.XPATH,"EmployeeId")
    # Methods
    def is_dashboard_displayed(self):
        dashboard = self.wait.until(EC.presence_of_element_located(self.DASHBOARD))
        return dashboard.is_displayed()

    def click_employee_button(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.EMPLOYEE_BUTTON))
        btn.click()

    def click_usermenu(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.USERMENU_BUTTON))
        btn.click()

    def click_logout(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.LOGOUT_BUTTON))
        btn.click()
