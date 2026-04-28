from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver


class TextBox:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def textBox(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.visibility_of_element_located((By.ID, "fullname"))).send_keys("Rohan Kumar")
        wait.until(EC.visibility_of_element_located((By.ID, "email"))).send_keys("rohankumar112@gmail.com")
        wait.until(EC.visibility_of_element_located((By.ID, "address"))).send_keys("Mandi Parishad Rd Vibhuti Khand, Gomti Nagar")
        wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys("12344")
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Submit']"))).click()