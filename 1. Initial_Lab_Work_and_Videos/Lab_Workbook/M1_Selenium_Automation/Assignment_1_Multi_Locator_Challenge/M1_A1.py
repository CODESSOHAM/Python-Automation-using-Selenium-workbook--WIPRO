from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

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

# 1. Locate Name using By.ID
name = driver.find_element(By.ID, "name")
name.send_keys("Soham")

# 2. Locate Email using By.ID
email = driver.find_element(By.ID, "email")
email.send_keys("soham@example.com")

# 3. Locate Male radio button using XPath
male = driver.find_element(By.XPATH, "//input[@id='male']")
male.click()


# Verification
print("Name:", name.get_attribute("value"))
print("Email:", email.get_attribute("value"))
print("Male selected:", male.is_selected())

time.sleep(5)
driver.quit()