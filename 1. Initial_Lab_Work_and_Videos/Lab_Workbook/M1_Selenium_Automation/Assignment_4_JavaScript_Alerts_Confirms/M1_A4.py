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


# Simple alert
alert_button = driver.find_element(By.XPATH, "//button[@id='alertBtn']")
alert_button.click()

alert = driver.switch_to.alert
print("Alert Message:", alert.text)

alert.accept()
print("Alert accepted")

print()


# Confirmation alert
confirm_button = driver.find_element(By.XPATH, "//button[@id='confirmBtn']")
confirm_button.click()

confirm = driver.switch_to.alert
print("Confirm Message:", confirm.text)

confirm.dismiss()
print("Confirm dismissed")

print()


# Prompt Popup
prompt_button = driver.find_element(By.XPATH, "//button[@id='promptBtn']")
prompt_button.click()

prompt = driver.switch_to.alert
print("Prompt message:", prompt.text)

prompt.send_keys("Soham Aich")
prompt.accept()
print("Prompt text entered and accepted")



time.sleep(5)
driver.quit()