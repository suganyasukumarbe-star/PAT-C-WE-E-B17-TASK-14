from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class BasePage:
    """Base class containing shared attributes and wrappers for explicit waits."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # 10-second explicit wait globally

    def wait_for_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))


class LoginPage(BasePage):
    """Page Object for the Zen Portal Login Screen."""

    # Locators — UPDATE THESE WITH YOUR PORTAL'S ACTUAL LOCATORS
    USERNAME_BOX = (By.NAME, "username")
    PASSWORD_BOX = (By.NAME, "password")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
    ERROR_MESSAGE = (By.ID, "error-msg")  # Object representing negative login failures

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://guvi.in"  # UPDATE WITH ACTUAL ZEN PORTAL URL

    def load(self):
        self.driver.get(self.url)

    def is_username_box_visible(self):
        try:
            return self.wait_for_element(self.USERNAME_BOX).is_displayed()
        except (TimeoutException, NoSuchElementException):
            return False

    def is_password_box_visible(self):
        try:
            return self.wait_for_element(self.PASSWORD_BOX).is_displayed()
        except (TimeoutException, NoSuchElementException):
            return False

    def is_submit_button_enabled(self):
        try:
            return self.wait_for_clickable(self.SUBMIT_BUTTON).is_enabled()
        except (TimeoutException, NoSuchElementException):
            return False

    def login(self, username, password):
        """Performs login action step sequence."""
        self.wait_for_element(self.USERNAME_BOX).clear()
        self.wait_for_element(self.USERNAME_BOX).send_keys(username)
        self.wait_for_element(self.PASSWORD_BOX).clear()
        self.wait_for_element(self.PASSWORD_BOX).send_keys(password)
        self.wait_for_clickable(self.SUBMIT_BUTTON).click()


class DashboardPage(BasePage):
    """Page Object for the Post-Login Zen Dashboard view."""

    # Locators — UPDATE THESE WITH YOUR PORTAL'S ACTUAL LOCATORS
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Logout')]")
    DASHBOARD_INDICATOR = (By.ID, "dashboard-main")

    def is_logged_in(self):
        try:
            return self.wait_for_element(self.DASHBOARD_INDICATOR).is_displayed()
        except (TimeoutException, NoSuchElementException):
            return False

    def logout(self):
        self.wait_for_clickable(self.LOGOUT_BUTTON).click()
