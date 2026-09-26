from behave import given, when, then
import requests
import json


BASE_URL = "https://jsonplaceholder.typicode.com"


@given("I load the API test data")
def step_load_test_data(context):

    with open("features/test_data.json", "r") as file:
        context.test_data = json.load(file)

    print("\nTest data loaded:")
    print(context.test_data)


@when("I send GET requests for all post IDs")
def step_send_get_requests(context):

    context.responses = []

    for data in context.test_data:
        post_id = data["post_id"]

        url = BASE_URL + "/posts/" + str(post_id)

        response = requests.get(url)

        context.responses.append(response)

        print("\nRequest URL:", url)
        print("Status Code:", response.status_code)


@then("all API responses should have status code 200")
def step_validate_responses(context):

    for response in context.responses:

        assert response.status_code == 200

        data = response.json()

        print("Returned Post ID:", data["id"])

        assert data["id"] > 0

    print("\nAll API responses validated successfully")
