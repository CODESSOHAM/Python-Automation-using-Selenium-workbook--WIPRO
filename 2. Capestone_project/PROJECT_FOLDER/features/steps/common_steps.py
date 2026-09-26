from behave import then

from framework.utils import (
    assert_api_response_code,
    assert_json_contains,
    assert_response_message_contains,
    assert_status_code,
)


@then("the response code should be {code:d}")
def step_check_status_code(context, code):
    """
    Checks the real HTTP status code. Use this for APIs that return normal
    REST status codes, e.g. jsonplaceholder (features/user_management.feature).
    """
    assert_status_code(context.response, code)


@then("the API response code should be {code:d}")
def step_check_api_response_code(context, code):
    """
    Checks the responseCode field inside the JSON body. Use this for
    automationexercise.com, which always returns real HTTP 200 and reports
    the true result inside the body instead.
    """
    assert_api_response_code(context.response, code)


@then('the response JSON should contain "{key}"')
def step_response_json_contains_key(context, key):
    assert_json_contains(context.response, key)


@then('the response message should contain "{expected_text}"')
def step_response_message_contains(context, expected_text):
    assert_response_message_contains(context.response, expected_text)
