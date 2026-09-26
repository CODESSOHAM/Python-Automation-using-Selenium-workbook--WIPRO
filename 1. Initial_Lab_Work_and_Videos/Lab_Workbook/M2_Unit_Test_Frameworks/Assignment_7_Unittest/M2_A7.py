import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager



class TestLogin(unittest.TestCase):

    def setUp(self):
        browsername = "chrome"

        if browsername.lower() == "chrome":
            self.driver = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install())
            )
        elif browsername.lower() == "firefox":
            self.driver = webdriver.Firefox(
                service=FirefoxService(GeckoDriverManager().install())
            )
        else:
            raise Exception("Invalid browser name.")

        self.driver.get("https://testautomationpractice.blogspot.com/")
        self.driver.maximize_window()


    def test_page_title(self):
        title = self.driver.title
        print("Page Title:", title)

        self.assertIn("Automation Testing Practice", title)


    def test_page_url(self):
        url = self.driver.current_url
        print("Page URL:", url)

        self.assertIn("testautomationpractice.blogspot.com", url)


    def test_logo_present(self):
        logo = self.driver.find_element(By.XPATH, "//h1[contains(text(), 'Automation Testing Practice')]")
        self.assertTrue(logo.is_displayed())
        self.assertTrue(logo.is_displayed)
        print("Logo/Heading is displayed")


    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()