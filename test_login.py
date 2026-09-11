import pytest
from pages import LoginPage, DashboardPage


@pytest.mark.usefixtures("init_driver")
class TestZenPortalLogin:

    @pytest.fixture(autouse=True)
    def setup_pages(self):
        """Instantiates required page structures prior to running test execution."""
        self.login_page = LoginPage(self.driver)
        self.dashboard_page = DashboardPage(self.driver)
        self.login_page.load()

    def test_validate_input_boxes(self):
        """Requirement 5c: Validate Username and Password Input boxes visibility."""
        assert self.login_page.is_username_box_visible(), "Username field missing"
        assert self.login_page.is_password_box_visible(), "Password field missing"

    def test_validate_submit_button(self):
        """Requirement 5d: Validate Submit button functionality state."""
        assert self.login_page.is_submit_button_enabled(), "Submit button is non-interactable"

    def test_unsuccessful_login(self):
        """Requirement 5b: Negative Login validation scenario."""
        self.login_page.login("invalid_user@gmail.com", "WrongPassword123")
        # Assert user stays on page or error is thrown instead of reaching dashboard
        assert not self.dashboard_page.is_logged_in(), "Logged into dashboard using illegal credentials"

    def test_successful_login_and_logout(self):
        """Requirement 5a & 5e: Validate successful entry followed immediately by logging out."""
        # Provide your verified system workspace user profiles below
        VALID_USER = "your_actual_username"
        VALID_PASS = "your_actual_password"

        # 1. Login Process
        self.login_page.login(VALID_USER, VALID_PASS)
        assert self.dashboard_page.is_logged_in(), "Login verification phase failed"

        # 2. Logout Process
        self.dashboard_page.logout()
        assert self.login_page.is_username_box_visible(), "Logout verification phase failed"
