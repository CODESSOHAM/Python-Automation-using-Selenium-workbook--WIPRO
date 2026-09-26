from behave import when


@when('I search for the product "{term}"')
def step_search_for_product(context, term):
    context.response = context.ae_client.search_product(term)


@when("I search for a product without providing the search term")
def step_search_without_term(context):
    context.response = context.ae_client.search_product(search_term=None)
