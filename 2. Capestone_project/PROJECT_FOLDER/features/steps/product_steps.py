from behave import given, when


@given("the Automation Exercise API is available")
def step_ae_api_available(context):
    assert context.ae_client is not None


@when("I send a GET request to the products list endpoint")
def step_get_products_list(context):
    context.response = context.ae_client.get_products_list()


@when("I send a POST request to the products list endpoint")
def step_post_products_list(context):
    context.response = context.ae_client.post_products_list()


@when("I send a GET request to the brands list endpoint")
def step_get_brands_list(context):
    context.response = context.ae_client.get_brands_list()


@when("I send a PUT request to the brands list endpoint")
def step_put_brands_list(context):
    context.response = context.ae_client.put_brands_list()
