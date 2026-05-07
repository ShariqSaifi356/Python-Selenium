from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def get_driver(browser):

    if browser == "chrome":
        chrome_options = ChromeOptions()

        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False  
        }

        chrome_options.add_experimental_option("prefs", prefs)

        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-save-password-bubble")
        chrome_options.add_argument("--incognito")  

        driver = webdriver.Chrome(options=chrome_options)

    elif browser == "firefox":
        firefox_options = FirefoxOptions()
        driver = webdriver.Firefox(options=firefox_options)

    else:
        raise ValueError(f"Browser {browser} not supported")

    driver.maximize_window()
    return driver