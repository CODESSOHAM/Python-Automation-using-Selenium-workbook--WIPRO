from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

browsername = "chrome"

if browsername.lower() == "chrome":
    driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
elif browsername.lower()=="firefox":
    driver=webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
else:
    raise Exception("Invalid browser name.")


driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()


# Find all checkboxes
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print("Total checkboxes:", len(checkboxes))

for checkbox in checkboxes:
    if not checkbox.is_selected():
        checkbox.click()

# Verify selected checkboxes
selected_count = 0
for checkbox in checkboxes:
    if checkbox.is_selected():
        selected_count += 1

print("Selected checkboxes:", selected_count)


print()


# Scrolling Dropdown
dropdown = driver.find_element(
    By.XPATH, "//input[@placeholder='Select an item']"
)
dropdown.click()

time.sleep(2)

# Find Item 50
item = driver.find_element(
    By.XPATH, "//*[normalize-space()='Item 50']"
)
item.click()
print("Selected Item 50")



time.sleep(5)
driver.quit()