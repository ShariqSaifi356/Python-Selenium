import pytest
from utils.driver_factory import get_driver

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests"
    )
    
@pytest.fixture
def setup(request):
    browser = request.config.getoption("--browser")
    driver = get_driver(browser)

    driver.get("https://the-internet.herokuapp.com/")
    yield driver
    driver.quit()