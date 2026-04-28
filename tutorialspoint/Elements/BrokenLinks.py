from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

class BrokenLinks:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def countTotalLinksOnThePage(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Broken Links - Images']"))).click()
        links = self.driver.find_elements(By.XPATH, "//div[@class='col-md-8 col-lg-8 col-xl-8']//a")
        print("Total links:", len(links))
        # Printing the text of links
        for link in links:
            print(link.text)
        