import json
import os

from behave import when

from framework.config import Config

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "test_data", "login_credentials.json")

with open(DATA_PATH) as f:
    LOGIN_DATA = json.load(f)


@when("I verify login with valid credentials")
def step_login_valid(context):
    creds = LOGIN_DATA["valid"]
    context.response = context.ae_client.verify_login(
        email=creds.get("email", Config.VALID_EMAIL),
        password=creds.get("password", Config.VALID_PASSWORD),
    )


@when("I verify login with invalid credentials")
def step_login_invalid(context):
    creds = LOGIN_DATA["invalid"]
    context.response = context.ae_client.verify_login(
        email=creds["email"], password=creds["password"]
    )


@when("I verify login using only a password")
def step_login_missing_email(context):
    context.response = context.ae_client.verify_login(email=None, password="SomePassword123")


@when("I send a DELETE request to verify login")
def step_delete_verify_login(context):
    context.response = context.ae_client.delete_verify_login()
