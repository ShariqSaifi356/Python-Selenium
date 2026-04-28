from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

class Links:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def newWindows(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Links']"))).click()
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Home']").click()
        windowsOpened = self.driver.window_handles
        self.driver.switch_to.window(windowsOpened[1])
        title  = self.driver.title
        print(f"The Title of the new opened child window is: {title}")
        assert title == "Coding Practice Problems & Tutorials | TutorialsPoint"
        self.driver.close()
        self.driver.switch_to.window(windowsOpened[0])
        parentTitle  = self.driver.title
        print(f"The Title of the parent window is: {parentTitle}")
        assert parentTitle == "Selenium Practice - Links"

    def textValidation(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@id='created']"))).click()
        createdText = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='create']"))).text
        assert createdText == "Link has responded with staus 201 and status text Created"

        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@id='no-content']"))).click()
        noContentText = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='nocontent']"))).text
        assert noContentText == "Link has responded with staus 204 and status text No Content"

        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@id='moved']"))).click()
        movedText = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "//div[@class='move']"))).text
        assert movedText == "Link has responded with staus 301 and status text Moved Permanently"