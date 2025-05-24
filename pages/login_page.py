from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    URL = "http://coditech-stage-admin.coditech.co.in/"

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)

    # Locators
    USERNAME_INPUT = (By.ID, "UserName")
    PASSWORD_INPUT = (By.ID, "Password")
    LOGIN_BUTTON = (By.CSS_SELECTOR,'.btn.btn-primary.w-100.waves-effect.waves-light')
    DASHBOARD = (By.XPATH, "//div[@class='page-content']")


    # Methods
    def load(self):
        self.browser.get(self.URL)

    def enter_username(self, username):
        elem = self.wait.until(EC.presence_of_element_located(self.USERNAME_INPUT))
        elem.clear()
        elem.send_keys(username)

    def enter_password(self, password):
        elem = self.wait.until(EC.presence_of_element_located(self.PASSWORD_INPUT))
        elem.clear()
        elem.send_keys(password)

    def click_login(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON))
        btn.click()

    def is_dashboard_displayed(self):
        dashboard = self.wait.until(EC.presence_of_element_located(self.DASHBOARD))
        return dashboard.is_displayed()

    def is_login_page_displayed(self):
        return self.browser.find_element(*self.LOGIN_BUTTON).is_displayed()


