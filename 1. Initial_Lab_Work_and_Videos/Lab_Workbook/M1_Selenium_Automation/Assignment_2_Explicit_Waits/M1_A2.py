from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

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


# Create explicit wait
wait = WebDriverWait(driver, 10)

# Wait until Name field is visible
name = wait.until(
    EC.visibility_of_element_located((By.ID, "name"))
)
# Enter name
name.send_keys("Soham Aich")
print("Name entered successfully")


# Wait until Email field is clickable
email = wait.until(
    EC.element_to_be_clickable((By.ID, "email"))
)
# Enter email
email.send_keys("soham@example.com")
print("Email entered successfully")

driver.quit()