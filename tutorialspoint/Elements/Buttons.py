from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains


class Buttons:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def simpleButton(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Elements']"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Buttons']"))).click()
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Click Me']").click()
        txt = wait.until(EC.presence_of_element_located((By.ID, "welcomeDiv"))).text
        assert txt == "You have done a dynamic click"
        print(f"You just clicked on a simple button and after the click text appeared: {txt}")

    def rightClickOnButton(self):
        wait = WebDriverWait(self.driver, 15)
        rightClick = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Right Click Me']")))
        ActionChains(self.driver).context_click(rightClick).perform()
    
    def doubleClickOnButton(self):
        wait = WebDriverWait(self.driver, 15)
        doubleClick = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Double Click Me']")))
        ActionChains(self.driver).double_click(doubleClick).perform()
        txt = wait.until(EC.presence_of_element_located((By.ID, "doublec"))).text
        assert txt == "You have Double clicked"
        print(f"You just double clicked on a doubleClick button and after the double click text appeared: {txt}")