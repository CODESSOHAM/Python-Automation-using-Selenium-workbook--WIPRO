"""
This is NOT part of the Behave suite. It's a quick offline check (using the
`responses` library to mock HTTP) proving the framework's client + assertion
logic is correct, since this sandbox has no network access to the real
jsonplaceholder / automationexercise domains. Run the real Behave suite on a
machine with internet access to hit the live APIs.
"""
import responses

from framework.api_client import AutomationExerciseClient, UserManagementClient
from framework.utils import assert_json_contains, assert_response_message_contains, assert_status_code


@responses.activate
def test_get_all_products():
    responses.add(
        responses.GET,
        "https://automationexercise.com/api/productsList",
        json={"responseCode": 200, "products": [{"id": 1, "name": "Blue Top"}]},
        status=200,
    )
    client = AutomationExerciseClient()
    r = client.get_products_list()
    assert_status_code(r, 200)
    assert_json_contains(r, "products")
    print("PASS: get_all_products")


@responses.activate
def test_post_products_list_405():
    responses.add(
        responses.POST,
        "https://automationexercise.com/api/productsList",
        json={"responseCode": 405, "message": "This request method is not supported."},
        status=200,  # site returns 200 wrapper w/ responseCode 405 in body historically; we just check message
    )
    client = AutomationExerciseClient()
    r = client.post_products_list()
    assert_response_message_contains(r, "not supported")
    print("PASS: post_products_list_405 message check")


@responses.activate
def test_search_product_missing_param():
    responses.add(
        responses.POST,
        "https://automationexercise.com/api/searchProduct",
        json={"responseCode": 400, "message": "Bad request, search_product parameter is missing in POST request."},
        status=200,
    )
    client = AutomationExerciseClient()
    r = client.search_product(search_term=None)
    assert_response_message_contains(r, "search_product parameter is missing")
    print("PASS: search_product_missing_param")


@responses.activate
def test_verify_login_valid():
    responses.add(
        responses.POST,
        "https://automationexercise.com/api/verifyLogin",
        json={"responseCode": 200, "message": "User exists!"},
        status=200,
    )
    client = AutomationExerciseClient()
    r = client.verify_login(email="a@b.com", password="pw")
    assert_status_code(r, 200)
    assert_response_message_contains(r, "User exists")
    print("PASS: verify_login_valid")


@responses.activate
def test_get_all_users():
    responses.add(
        responses.GET,
        "https://jsonplaceholder.typicode.com/users",
        json=[{"id": 1, "name": "Leanne Graham"}],
        status=200,
    )
    client = UserManagementClient()
    r = client.get_all_users()
    assert_status_code(r, 200)
    body = r.json()
    assert isinstance(body, list) and len(body) == 1
    print("PASS: get_all_users")


@responses.activate
def test_create_user():
    responses.add(
        responses.POST,
        "https://jsonplaceholder.typicode.com/users",
        json={"id": 11, "name": "Jane Doe"},
        status=201,
    )
    client = UserManagementClient()
    r = client.create_user({"name": "Jane Doe"})
    assert_status_code(r, 201)
    assert_json_contains(r, "name", "Jane Doe")
    print("PASS: create_user")


if __name__ == "__main__":
    test_get_all_products()
    test_post_products_list_405()
    test_search_product_missing_param()
    test_verify_login_valid()
    test_get_all_users()
    test_create_user()
    print("\nALL OFFLINE SMOKE TESTS PASSED")
