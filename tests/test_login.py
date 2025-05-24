from pages.employee_page import EmployeePage
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_valid_login(browser):
    login_page = LoginPage(browser)
    login_page.load()
    login_page.enter_username("superadmin@gmail.com")
    login_page.enter_password("user@123")
    login_page.click_login()

    assert login_page.is_dashboard_displayed()

def test_valid_logout(browser):
    login_page = LoginPage(browser)
    login_page.load()
    login_page.enter_username("superadmin@gmail.com")
    login_page.enter_password("user@123")
    login_page.click_login()
    dashboard_page = DashboardPage(browser)
    dashboard_page.click_usermenu()
    # dashboard_page.click_logout()

    assert login_page.is_login_page_displayed()

def test_navigate_to_employee(browser):
    login_page = LoginPage(browser)
    dashboard_page = DashboardPage(browser)

    # Step 1: Login
    login_page.load()
    login_page.enter_username("superadmin@gmail.com")
    login_page.enter_password("user@123")
    login_page.click_login()

    assert login_page.is_dashboard_displayed()

    # Step 2: Navigate to Employee
    dashboard_page.click_employee_button()

    assert "employeemaster/list" in browser.current_url.lower()

def test_create_employee(browser):
    login = LoginPage(browser)
    dashboard = DashboardPage(browser)
    employee_page = EmployeePage(browser)

    login.load()
    login.enter_username("superadmin@gmail.com")
    login.enter_password("user@123")
    login.click_login()
    assert login.is_dashboard_displayed()

    dashboard.click_employee_button()
    assert "employeemaster/list" in browser.current_url.lower()

    employee_page.click_create_employee_button()
    assert "employeemaster/createemployee" in browser.current_url.lower()

    # Fill and submit the form
    employee_page.fill_create_employee_form(
        centre_name="Testing Account Centre",
        title="Miss",
        first_name="John",
        last_name="Doe",
        gender="Male",
        email="joedoe@yopmail.com",
        callingcode="+91",
        mobile="9876543210",

    )



