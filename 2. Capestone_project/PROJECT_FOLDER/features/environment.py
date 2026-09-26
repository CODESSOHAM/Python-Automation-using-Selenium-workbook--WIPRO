"""
Behave hooks.

- before_all: nothing global needed beyond logging setup.
- before_scenario: attach fresh client instances to `context` so step
  definitions share state within a scenario but never leak it across
  scenarios.
- after_step: attach the last request/response info to the Allure report
  (if allure is installed and active) so every step's evidence is visible
  in the HTML report.
"""

import json

from framework.api_client import AutomationExerciseClient, UserManagementClient
from framework.logger import get_logger

logger = get_logger("environment")

try:
    import allure

    ALLURE_AVAILABLE = True
except ImportError:
    ALLURE_AVAILABLE = False


def before_all(context):
    logger.info("Starting test run")


def before_scenario(context, scenario):
    context.user_client = UserManagementClient()
    context.ae_client = AutomationExerciseClient()
    context.response = None
    logger.info("Starting scenario: %s", scenario.name)


def after_step(context, step):
    if not ALLURE_AVAILABLE:
        return
    response = getattr(context, "response", None)
    if response is None:
        return
    try:
        body_preview = json.dumps(response.json(), indent=2)
    except ValueError:
        body_preview = response.text

    allure.attach(
        f"URL: {response.url}\nStatus: {response.status_code}\n\nBody:\n{body_preview}",
        name=f"Response for step: {step.name}",
        attachment_type=allure.attachment_type.TEXT,
    )


def after_scenario(context, scenario):
    logger.info("Finished scenario: %s -> %s", scenario.name, scenario.status)


def after_all(context):
    logger.info("Test run complete")
