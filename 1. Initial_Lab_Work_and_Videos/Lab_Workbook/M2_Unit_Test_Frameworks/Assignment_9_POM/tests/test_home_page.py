import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from Assignment_9_POM.pages.home_page import HomePage


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



def test_page_title(driver):
    home_page = HomePage(driver)

    title = home_page.get_page_title()
    print("Page Title:", title)

    assert "Automation Testing Practice" in title



def test_page_url(driver):
    home_page = HomePage(driver)

    url = home_page.get_page_url()
    print("Page URL:", url)

    assert "testautomationpractice.blogspot.com" in url



def test_heading_displayed(driver):
    home_page = HomePage(driver)

    heading = home_page.get_heading()
    print("Page Heading:", heading.text)

    assert heading.is_displayed()
