import json
import os

from behave import given, then, when

from framework.utils import assert_json_contains

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "test_data", "users.json")

with open(DATA_PATH) as f:
    USER_DATA = json.load(f)


@given("the User Management API is available")
def step_user_api_available(context):
    assert context.user_client is not None


@when("I request all users")
def step_get_all_users(context):
    context.response = context.user_client.get_all_users()


@when('I request the user with id {user_id:d}')
def step_get_user_by_id(context, user_id):
    context.response = context.user_client.get_user(user_id)


@when("I create a new user with the sample payload")
def step_create_user(context):
    context.response = context.user_client.create_user(USER_DATA["new_user"])


@when('I update user {user_id:d} with the updated payload')
def step_update_user(context, user_id):
    context.response = context.user_client.update_user(user_id, USER_DATA["updated_user"])


@when('I delete user {user_id:d}')
def step_delete_user(context, user_id):
    context.response = context.user_client.delete_user(user_id)


@then("the response should contain a list of users")
def step_response_is_user_list(context):
    body = context.response.json()
    assert isinstance(body, list) and len(body) > 0, "Expected a non-empty list of users"


@then('the user response should contain field "{field}" with value {value}')
def step_user_field_equals(context, field, value):
    # Try to interpret the value as an int if possible, else keep as string
    try:
        expected = int(value)
    except ValueError:
        expected = value.strip('"')
    assert_json_contains(context.response, field, expected)
