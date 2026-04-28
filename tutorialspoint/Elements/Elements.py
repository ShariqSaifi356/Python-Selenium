import time
from selenium import webdriver
from TextBox import TextBox
from CheckBox import CheckBox
from RadioButton import RadioButton
from WebTables import WebTables
from Buttons import Buttons
from Links import Links
from BrokenLinks import BrokenLinks

class Elements:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.tutorialspoint.com/selenium/practice/text-box.php")
        self.driver.maximize_window()

    def waitTimeAndQuit(self):
        time.sleep(5)
        self.driver.quit()


obj = Elements()

textbox = TextBox(obj.driver)
textbox.textBox()

checkbox = CheckBox(obj.driver)
checkbox.checkBox()

radio = RadioButton(obj.driver)
radio.radioButton()

tables = WebTables(obj.driver)
tables.deleteAllRowsInATables()
tables.addNewRowInATable()

buttons = Buttons(obj.driver)
buttons.simpleButton()
buttons.rightClickOnButton()
buttons.doubleClickOnButton()

links = Links(obj.driver)
links.newWindows()
links.textValidation()

brokenLinks = BrokenLinks(obj.driver)
brokenLinks.countTotalLinksOnThePage()

obj.waitTimeAndQuit()