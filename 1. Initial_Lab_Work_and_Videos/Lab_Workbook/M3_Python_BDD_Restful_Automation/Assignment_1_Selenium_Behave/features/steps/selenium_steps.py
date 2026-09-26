from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager



@given("I open the automation practice website")
def step_open_website(context):
    context.driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )

    context.driver.maximize_window()

    context.driver.get(
        "https://testautomationpractice.blogspot.com/"
    )

    print("\nAutomation Practice website opened")



@when("I enter my name")
def step_enter_name(context):
    name_field = context.driver.find_element(
        By.ID, "name"
    )

    name_field.send_keys("Soham Aich")

    print("Name entered")



@when("I enter my email")
def step_enter_email(context):
    email_field = context.driver.find_element(
        By.ID, "email"
    )

    email_field.send_keys("soham@example.com")

    print("Email entered")



@when("I enter my phone number")
def step_enter_phone(context):
    phone_field = context.driver.find_element(
        By.ID, "phone"
    )

    phone_field.send_keys("7003659480")

    print("Phone number entered")



@when("I select the male gender")
def step_select_gender(context):
    male_radio = context.driver.find_element(
        By.ID, "male"
    )

    male_radio.click()

    print("Male gender selected")



@then("the form data should be entered successfully")
def step_validate_form(context):

    name_value = context.driver.find_element(
        By.ID, "name"
    ).get_attribute("value")

    email_value = context.driver.find_element(
        By.ID, "email"
    ).get_attribute("value")

    phone_value = context.driver.find_element(
        By.ID, "phone"
    ).get_attribute("value")

    gender_selected = context.driver.find_element(
        By.ID, "male"
    ).is_selected()

    assert name_value == "Soham Aich"
    assert email_value == "soham@example.com"
    assert phone_value == "7003659480"
    assert gender_selected

    print("Form validation passed")
    context.driver.quit()
