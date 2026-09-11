import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="class")
def init_driver(request):
    """Initializes the Chrome WebDriver instance."""
    options = webdriver.ChromeOptions()
    # Add options here if needed (e.g., options.add_argument("--headless"))
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()
