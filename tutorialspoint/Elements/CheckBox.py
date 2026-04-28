from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver

class CheckBox:

    def __init__(self, driver: WebDriver):
        self.driver = driver
    
    def checkBox(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Elements']"))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[normalize-space()='Check Box']"))).click()
        mainlevel1 = wait.until(EC.visibility_of_element_located((By.ID, "c_bs_1"))).is_selected()
        if mainlevel1 is False:
            self.driver.find_element(By.ID, "c_bs_1").click()
        else:
            print("Check Box is already ticked!")

        self.driver.find_element(By.CSS_SELECTOR, "body > main:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(1) > span:nth-child(1)").click()
        sublevel1 = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='c_bf_1']"))).is_selected()
        if sublevel1 is True:
            print("Sub level check box is already ticked.")
        else:
            print("Sub level check box is not ticked.")