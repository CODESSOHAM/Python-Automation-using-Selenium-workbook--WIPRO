import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture
def driver():
    browsername = "chrome"
    
    if browsername.lower() == "chrome":
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install())
        )
    elif browsername.lower() == "firefox":
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install())
        )
    else:
        raise Exception("Invalid browser name.")
    
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.maximize_window()


    yield driver

    driver.quit()



@pytest.mark.smoke
def test_page_title(driver):
    title = driver.title
    print("Page Title:", title)

    assert "Automation Testing Practice" in title



@pytest.mark.regression
def test_page_url(driver):
    url = driver.current_url
    print("Page URL", url)

    assert "testautomationpractice.blogspot.com" in url



@pytest.mark.regression
def test_heading_displayed(driver):
    heading = driver.find_element(By.XPATH, "//h1[contains(text(),'Automation Testing Practice')]")
    print("Page heading:", heading.text)

    assert heading.is_displayed()
