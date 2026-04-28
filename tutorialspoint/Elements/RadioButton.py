from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver


class RadioButton:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def radioButton(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Radio Button']"))).click()
        assert not self.driver.find_element(By.XPATH, "//input[@value='igottwo']").is_selected()
        print(f'''Radio Button is selected or not : {self.driver.find_element(By.XPATH, "//input[@value='igottwo']").is_selected()}''')
        self.driver.find_element(By.XPATH, "//input[@value='igottwo']").click()
        print(self.driver.find_element(By.XPATH, "//div[@id='check']").text)
        assert self.driver.find_element(By.XPATH, "//div[@id='check']").text == "You have checked Yes"
        assert not self.driver.find_element(By.XPATH, "//input[@name='inlineRadioOptions']").is_enabled()
        print(f'''Radio button is enabled or not: {self.driver.find_element(By.XPATH, "//input[@name='inlineRadioOptions']").is_enabled()}''')
        