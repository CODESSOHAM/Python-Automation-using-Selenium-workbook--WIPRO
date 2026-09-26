"""
Generic, reusable API client.

Step definitions never call `requests` directly - they go through an
instance of APIClient. This means:
  * Base URL, headers, timeout, and session handling live in one place.
  * Swapping to a different API only means instantiating APIClient with
    a different base_url (see UserManagementClient / AutomationExerciseClient
    below, which are thin, endpoint-aware wrappers on top of APIClient).
  * Logging and error handling are consistent everywhere.
"""

import requests

from framework.config import Config
from framework.endpoints import AutomationExerciseEndpoints, JSONPlaceholderEndpoints
from framework.logger import get_logger

logger = get_logger(__name__)


class APIClient:
    """Thin, generic wrapper around requests.Session for one base URL."""

    def __init__(self, base_url: str, headers: dict | None = None, timeout: int | None = None):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update(headers or Config.DEFAULT_HEADERS)
        self.timeout = timeout or Config.TIMEOUT

    def _url(self, endpoint: str) -> str:
        return f"{self.base_url}{endpoint}"

    def get(self, endpoint: str, params: dict | None = None, **kwargs) -> requests.Response:
        url = self._url(endpoint)
        logger.info("GET %s params=%s", url, params)
        response = self.session.get(url, params=params, timeout=self.timeout, **kwargs)
        self._log_response(response)
        return response

    def post(self, endpoint: str, data: dict | None = None, json: dict | None = None, **kwargs) -> requests.Response:
        url = self._url(endpoint)
        logger.info("POST %s data=%s json=%s", url, data, json)
        response = self.session.post(url, data=data, json=json, timeout=self.timeout, **kwargs)
        self._log_response(response)
        return response

    def put(self, endpoint: str, data: dict | None = None, json: dict | None = None, **kwargs) -> requests.Response:
        url = self._url(endpoint)
        logger.info("PUT %s data=%s json=%s", url, data, json)
        response = self.session.put(url, data=data, json=json, timeout=self.timeout, **kwargs)
        self._log_response(response)
        return response

    def patch(self, endpoint: str, data: dict | None = None, json: dict | None = None, **kwargs) -> requests.Response:
        url = self._url(endpoint)
        logger.info("PATCH %s data=%s json=%s", url, data, json)
        response = self.session.patch(url, data=data, json=json, timeout=self.timeout, **kwargs)
        self._log_response(response)
        return response

    def delete(self, endpoint: str, **kwargs) -> requests.Response:
        url = self._url(endpoint)
        logger.info("DELETE %s", url)
        response = self.session.delete(url, timeout=self.timeout, **kwargs)
        self._log_response(response)
        return response

    @staticmethod
    def _log_response(response: requests.Response) -> None:
        preview = response.text[:300].replace("\n", " ")
        logger.info("Response %s: %s", response.status_code, preview)


class UserManagementClient(APIClient):
    """Endpoint-aware client for the jsonplaceholder Users API (CRUD demo)."""

    def __init__(self):
        super().__init__(Config.JSONPLACEHOLDER_BASE_URL)

    def get_all_users(self):
        return self.get(JSONPlaceholderEndpoints.USERS)

    def get_user(self, user_id: int):
        return self.get(JSONPlaceholderEndpoints.USER_BY_ID.format(user_id=user_id))

    def create_user(self, payload: dict):
        return self.post(JSONPlaceholderEndpoints.USERS, json=payload)

    def update_user(self, user_id: int, payload: dict):
        return self.put(JSONPlaceholderEndpoints.USER_BY_ID.format(user_id=user_id), json=payload)

    def delete_user(self, user_id: int):
        return self.delete(JSONPlaceholderEndpoints.USER_BY_ID.format(user_id=user_id))


class AutomationExerciseClient(APIClient):
    """
    Endpoint-aware client for the automationexercise.com practice API.

    IMPORTANT: unlike jsonplaceholder, this API expects form-encoded POST
    bodies (application/x-www-form-urlencoded), not JSON. We must NOT force
    a Content-Type: application/json header here, or the server's $_POST
    parsing will silently receive nothing, no matter what values are
    actually sent - every request looks like a "missing parameter" request.
    Only "Accept" is set; `requests` will correctly auto-set the
    Content-Type to form-urlencoded whenever we pass data=<dict> for a POST.
    """

    def __init__(self):
        super().__init__(Config.AUTOMATIONEXERCISE_BASE_URL, headers={"Accept": "application/json"})

    def get_products_list(self):
        return self.get(AutomationExerciseEndpoints.PRODUCTS_LIST)

    def post_products_list(self):
        # Intentionally unsupported method -> expect 405
        return self.post(AutomationExerciseEndpoints.PRODUCTS_LIST)

    def get_brands_list(self):
        return self.get(AutomationExerciseEndpoints.BRANDS_LIST)

    def put_brands_list(self):
        # Intentionally unsupported method -> expect 405
        return self.put(AutomationExerciseEndpoints.BRANDS_LIST)

    def search_product(self, search_term: str | None = None):
        data = {"search_product": search_term} if search_term is not None else {}
        return self.post(AutomationExerciseEndpoints.SEARCH_PRODUCT, data=data)

    def verify_login(self, email: str | None = None, password: str | None = None):
        data = {}
        if email is not None:
            data["email"] = email
        if password is not None:
            data["password"] = password
        return self.post(AutomationExerciseEndpoints.VERIFY_LOGIN, data=data)

    def delete_verify_login(self):
        # Intentionally unsupported method -> expect 405
        return self.delete(AutomationExerciseEndpoints.VERIFY_LOGIN)
