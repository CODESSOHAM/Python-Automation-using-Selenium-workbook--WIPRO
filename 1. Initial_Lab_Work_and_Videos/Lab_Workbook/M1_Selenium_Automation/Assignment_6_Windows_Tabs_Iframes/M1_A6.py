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

driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe")
driver.maximize_window()
print("Main page title:", driver.title)
print("Main window:", driver.current_window_handle)
iframe = driver.find_element(By.XPATH, "//iframe[@id='iframeResult']")
driver.switch_to.frame(iframe)
print("Switched to iframe successfully")
driver.switch_to.default_content()
print("Switched back to main page")
print()
driver.switch_to.new_window("tab")
driver.get("https://www.google.com")
print("New tab opened")
print("New tab title:", driver.title)
print("New tab handle:", driver.current_window_handle)
print()
handles = driver.window_handles
print("Total windows/tabs:", len(handles))
for handle in handles:
    print("Window handles:", handle)

print()
driver.switch_to.window(handles[0])
print("Switched back to main window")
print("Main window title:", driver.title)
print()
driver.switch_to.window(handles[1])
print("Switched to new tab")
driver.close()
print("New tab closed")
print()
driver.switch_to.window(handles[0])
print("Returned to main window")
print("Final window title:", driver.title)
time.sleep(5)
driver.quit()