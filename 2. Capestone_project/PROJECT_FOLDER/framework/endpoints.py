"""
Endpoint constants.

Keeping every URL path in one place means that if an API version or path
changes, there is exactly one line to update.
"""


class JSONPlaceholderEndpoints:
    USERS = "/users"
    USER_BY_ID = "/users/{user_id}"


class AutomationExerciseEndpoints:
    PRODUCTS_LIST = "/productsList"
    BRANDS_LIST = "/brandsList"
    SEARCH_PRODUCT = "/searchProduct"
    VERIFY_LOGIN = "/verifyLogin"
