"""
Central configuration for the framework.

All environment-specific values (base URLs, timeouts, credentials) live
here and can be overridden via environment variables, so the same test
suite can run against dev/staging/prod without code changes.
"""

import os


class Config:
    # Base URLs for the two APIs used in this capstone
    JSONPLACEHOLDER_BASE_URL = os.getenv(
        "JSONPLACEHOLDER_BASE_URL", "https://jsonplaceholder.typicode.com"
    )
    AUTOMATIONEXERCISE_BASE_URL = os.getenv(
        "AUTOMATIONEXERCISE_BASE_URL", "https://automationexercise.com/api"
    )

    # Request behaviour
    TIMEOUT = int(os.getenv("API_TIMEOUT", "15"))
    DEFAULT_HEADERS = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    # Sample credentials for login-style tests (override via env vars in CI)
    VALID_EMAIL = os.getenv("TEST_USER_EMAIL", "testuser@example.com")
    VALID_PASSWORD = os.getenv("TEST_USER_PASSWORD", "TestPassword123")
