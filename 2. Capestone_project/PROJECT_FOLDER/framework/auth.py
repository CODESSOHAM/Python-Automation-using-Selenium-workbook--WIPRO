"""
Auth helpers.

Neither demo API used here requires a real bearer token, but real-world
User Management APIs usually do. This module keeps auth logic isolated
so swapping in a real OAuth/JWT flow later only touches this file.
"""

from framework.logger import get_logger

logger = get_logger(__name__)


def build_bearer_header(token: str) -> dict:
    """Return an Authorization header dict for a bearer token."""
    return {"Authorization": f"Bearer {token}"}


def extract_token_from_response(response) -> str | None:
    """
    Example helper for APIs that return a token on login.
    Not used by jsonplaceholder / automationexercise, but shown here so the
    framework is ready to plug into a real authenticated API.
    """
    try:
        body = response.json()
    except ValueError:
        logger.warning("Response was not JSON; cannot extract token")
        return None
    return body.get("token") or body.get("access_token")
