# contains Selenium locators and page actions.


from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

        self.name_field = (By.ID, "name")
        self.email_field = (By.ID, "email")
        self.phone_field = (By.ID, "phone")
        self.male_radio = (By.ID, "male")

    def enter_name(self, name):
        self.driver.find_element(*self.name_field).send_keys(name)

    def enter_email(self, email):
        self.driver.find_element(*self.email_field).send_keys(email)

    def enter_phone(self, phone):
        self.driver.find_element(*self.phone_field).send_keys(phone)

    def select_male_gender(self):
        self.driver.find_element(*self.male_radio).click()



    def get_name(self):
        return self.driver.find_element(
            *self.name_field
        ).get_attribute("value")

    def get_email(self):
        return self.driver.find_element(
            *self.email_field
        ).get_attribute("value")

    def get_phone(self):
        return self.driver.find_element(
            *self.phone_field
        ).get_attribute("value")

    def is_male_selected(self):
        return self.driver.find_element(
            *self.male_radio
        ).is_selected()
