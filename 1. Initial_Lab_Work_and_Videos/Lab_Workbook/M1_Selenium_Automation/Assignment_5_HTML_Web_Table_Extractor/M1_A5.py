
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



# Locate the table
rows = driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr")
print("Total rows:", len(rows))



# make the table extractor print headers + all rows neatly.
print("Book Details")
print("-"*50)

for row in rows:
    cols = row.find_elements(By.TAG_NAME, "td")

    for col in cols:
        print(col.text, end=" | ")

    print()

print("-"*50)
print()


# Find a particular book and retrieve its Price
book_name = "Master In Selenium"

for row in rows:
    cols = row.find_elements(By.TAG_NAME, "td")

    if len(cols) > 0 and cols[0].text == book_name:
        print("Book:", cols[0].text)
        print("Price:", cols[3].text)
        break

print("Book found successfully")



time.sleep(5)
driver.quit()