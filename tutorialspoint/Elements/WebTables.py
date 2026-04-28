from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

class WebTables:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def deleteAllRowsInATables(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Web Tables']"))).click()
        dataToBeDeleted = self.driver.find_elements(By.XPATH, "//div[@class='bd-example table-responsive']/table/tbody/tr/td/a[@title='delete']")
        print(f"No of Rows in a table are: {len(dataToBeDeleted)}")
        for i in range(len(dataToBeDeleted)):
            wait.until(EC.element_to_be_clickable((dataToBeDeleted[i]))).click()
    
    def addNewRowInATable(self):
        self.driver.implicitly_wait(5)
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Add']"))).click()
        self.driver.find_element(By.ID, "firstname").send_keys("Rohan")
        self.driver.find_element(By.ID, "lastname").send_keys("Kumar")
        self.driver.find_element(By.ID, "email").send_keys("rohankumar112@gmail.com")
        self.driver.find_element(By.ID, "age").send_keys("1232")
        self.driver.find_element(By.ID, "salary").send_keys("12322222222222222200")
        self.driver.find_element(By.ID, "deparment").send_keys("IT")
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        