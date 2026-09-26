"""
Reusable assertion and validation helpers shared by step definitions.
Keeping assertions here (rather than scattered across step files) means
error messages stay consistent and step definitions stay thin.
"""

import jsonschema

from framework.logger import get_logger

logger = get_logger(__name__)


def assert_status_code(response, expected_code: int):
    """
    Checks the REAL transport-level HTTP status code (the status line).
    Use this for APIs that follow normal REST conventions, e.g. jsonplaceholder.
    """
    actual = response.status_code
    assert actual == expected_code, (
        f"Expected HTTP status code {expected_code}, got {actual}. "
        f"Response body: {response.text[:300]}"
    )


def assert_api_response_code(response, expected_code: int):
    """
    Checks the APPLICATION-level response code embedded inside the JSON body
    under the "responseCode" key.

    Quirk of automationexercise.com/api: the site almost always replies with
    real HTTP 200, even for what it considers a 400/404/405 "failure". The
    true result lives in the JSON body's `responseCode` field instead of the
    HTTP status line, so tests against that API must assert on this, not on
    response.status_code.
    """
    try:
        body = response.json()
    except ValueError:
        raise AssertionError(
            f"Expected JSON body with responseCode {expected_code}, "
            f"but response was not valid JSON: {response.text[:300]}"
        )
    actual = body.get("responseCode")
    assert actual == expected_code, (
        f"Expected body responseCode {expected_code}, got {actual}. "
        f"Full body: {body}"
    )


def assert_json_contains(response, key: str, expected_value=None):
    body = response.json()
    assert key in body, f"Key '{key}' not found in response JSON: {body}"
    if expected_value is not None:
        assert body[key] == expected_value, (
            f"Expected '{key}' == {expected_value!r}, got {body[key]!r}"
        )


def assert_response_message_contains(response, expected_substring: str):
    """
    automationexercise.com responses are JSON but the field name for the
    message varies ('message' or 'responseMessage' depending on endpoint).
    This checks either field, or falls back to the raw text.
    """
    try:
        body = response.json()
    except ValueError:
        body = {}

    message = body.get("message") or body.get("responseMessage") or response.text
    assert expected_substring.lower() in str(message).lower(), (
        f"Expected message to contain '{expected_substring}', got: {message}"
    )


def validate_schema(instance: dict, schema: dict):
    try:
        jsonschema.validate(instance=instance, schema=schema)
    except jsonschema.exceptions.ValidationError as e:
        raise AssertionError(f"Schema validation failed: {e.message}")
