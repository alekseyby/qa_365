import os
import pytest
import allure
from selenium.webdriver import Chrome, Firefox
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

DEFAULT_WAIT_TIME = 10


def pytest_addoption(parser):
    parser.addoption("--browser_type", action="store", default="Chrome", help="Type in browser type")
    parser.addoption("--headless", action="store", default=True, help="Headless mode")
    parser.addoption("--file_log_level", default='WARNING', type=str, action="store", help="Headless mode")


@pytest.fixture(scope="session")
def log_level(request):
    return request.config.getoption("--file_log_level")


@pytest.fixture(scope="session", autouse=True)
def set_file_log_level(request, log_level):
    """ create environment variable to set log level in log_helper.py """
    os.environ['FILE_LOG_LEVEL'] = log_level
    yield
    del os.environ['FILE_LOG_LEVEL']


@pytest.fixture(scope="session")
def browser_type(request):
    return request.config.getoption("--browser_type")


@pytest.fixture(scope="session")
def headless(request):
    return request.config.getoption("--headless")


@allure.step("Open Browser")
@pytest.fixture
def browser(browser_type, headless):
    # Initialize WebDriver
    options = Options()
    if browser_type == 'Chrome':
        if headless:
            options.headless = True
        # FIXME
        # Workaround as I have old version of chrome browser
        driver = Chrome(ChromeDriverManager(version="108.0.5359.22").install(), options=options)

    elif browser_type == 'Firefox':
        driver = Firefox()
    else:
        raise Exception(f'{browser_type} is not a supported browser')
    # Wait implicitly for elements to be ready before attempting interactions
    driver.implicitly_wait(DEFAULT_WAIT_TIME)

    # Return the driver object at the end of setup
    yield driver

    # For cleanup, quit the driver
    driver.quit()
