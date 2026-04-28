from datetime import datetime
import base64
import pytest
import pytest_html
from utils.driver_factory import get_driver

# CLI option added for screenshot
# pytest -v --html=reports/report.html --self-contained-html --screenshot (Run this commad to take screenshot)
# pytest tests/negative_test/test_login_failed.py -v --html=reports/report_2.html --self-contained-html --screenshot
def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests"
    )
    parser.addoption(
        "--screenshot",
        action="store_true",
        help="Enable screenshots on failure"
    )
    

@pytest.fixture
def setup(request):
    browser = request.config.getoption("--browser")
    driver = get_driver(browser)

    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()
    
    
# Hook: Add screenshot ONLY if flag is passed
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        #Skip if flag not provided
        if not item.config.getoption("--screenshot"):
            return

        driver = item.funcargs.get("setup", None)

        if driver:
            #Clean test name
            safe_test_name = item.name.replace("[", "_").replace("]", "")

            #Timestamp
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

            #File path
            file_name = f"reports/screenshots/{safe_test_name}_{timestamp}.png"

            #Save screenshot
            driver.save_screenshot(file_name)

            #Embed screenshot (for self-contained HTML)
            with open(file_name, "rb") as image_file:
                encoded = base64.b64encode(image_file.read()).decode()

            extra = getattr(report, "extra", [])
            extra.append(pytest_html.extras.image(encoded, mime_type="image/png"))
            extra.append(pytest_html.extras.text("Test failed - check screenshot"))
            report.extra = extra