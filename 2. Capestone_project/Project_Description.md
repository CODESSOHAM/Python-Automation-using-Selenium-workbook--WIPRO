# Capstone Project: API Automation Framework

## Project Name

**API Automation Framework using Python, Requests, Behave BDD, and Allure**

## Objective

The objective of this project is to build a reusable API test automation framework that verifies REST API behavior through readable BDD scenarios. The framework demonstrates how Python can be used to automate positive and negative API tests, validate response content, check status codes, produce test evidence, and organize a test suite for future extension.

The project tests two public practice APIs:

1. **JSONPlaceholder** for user-management CRUD operations
2. **Automation Exercise API** for products, brands, product search, and login verification

## Project Description

This capstone project implements an end-to-end API automation solution. Test scenarios are written in Gherkin feature files so that each requirement can be read as a business-friendly behavior. Python step definitions connect those scenarios to reusable client methods, while the framework layer manages URLs, requests, configuration, logging, authentication helpers, and assertions.

The framework is designed to keep test intent separate from implementation details:

- Feature files describe **what** should happen.
- Step definitions connect Gherkin steps to Python behavior.
- API clients describe **how** requests are sent.
- Endpoint constants keep paths in one location.
- Assertion helpers provide consistent validation and error messages.
- Behave hooks manage scenario setup and reporting evidence.

This structure makes the project easier to read, maintain, debug, and extend with additional endpoints or APIs.

## APIs and Functional Coverage

### 1. JSONPlaceholder User Management API

The user-management feature demonstrates standard CRUD operations against the `/users` resource:

- Retrieve all users
- Retrieve one user by ID
- Create a new user
- Update an existing user
- Delete a user
- Verify the response for a user that does not exist

These scenarios validate normal REST-style HTTP status codes such as `200`, `201`, and `404`.

### 2. Automation Exercise API

The Automation Exercise features cover the following endpoints:

- `GET /productsList` to retrieve products
- Unsupported `POST /productsList` behavior
- `GET /brandsList` to retrieve brands
- Unsupported `PUT /brandsList` behavior
- `POST /searchProduct` with valid search terms
- Product search without the required parameter
- Login verification with valid credentials
- Login with a missing email or password
- Login with invalid credentials
- Unsupported `DELETE /verifyLogin` behavior

The search feature uses a Gherkin Scenario Outline to execute the same behavior with multiple terms such as `top`, `tshirt`, and `jean`.

## Detailed Explanation of the Framework

### Feature Layer

The `features/` directory contains the BDD specifications. Each `.feature` file groups related API behavior and uses tags such as `@smoke`, `@negative`, `@users`, `@products`, `@brands`, `@search`, and `@login`.

The feature files contain:

- Feature descriptions
- Business-readable user stories
- Background steps for API availability
- Positive and negative scenarios
- Expected response codes and response content
- Scenario Outline examples for repeated test data

### Step Definition Layer

The files in `features/steps/` implement the Gherkin steps. They create requests through the framework clients, store the latest response in Behave context, and call shared assertion functions. Step definitions stay intentionally thin so request construction and validation logic remain reusable.

### API Client Layer

`framework/api_client.py` contains a generic `APIClient` built on `requests.Session`. It centralizes:

- Base URL handling
- Shared request headers
- Request timeouts
- GET, POST, PUT, PATCH, and DELETE methods
- Request and response logging

Two endpoint-aware clients extend the generic client:

- `UserManagementClient` for JSONPlaceholder user operations
- `AutomationExerciseClient` for products, brands, search, and login operations

The Automation Exercise client correctly sends form-encoded POST data for endpoints that expect form parameters, while JSONPlaceholder user payloads are sent as JSON.

### Configuration Layer

`framework/config.py` stores base URLs, timeout settings, default headers, and sample login values. Environment variables can override these defaults, allowing the same framework to be used against different environments without changing source code.

Supported overrides include:

- `JSONPLACEHOLDER_BASE_URL`
- `AUTOMATIONEXERCISE_BASE_URL`
- `API_TIMEOUT`
- `TEST_USER_EMAIL`
- `TEST_USER_PASSWORD`

### Endpoint Layer

`framework/endpoints.py` contains endpoint path constants. Keeping paths in one module avoids repeated hard-coded URLs and makes API version or path changes easier to manage.

### Assertion and Validation Layer

`framework/utils.py` provides reusable validation helpers for:

- Real HTTP status codes
- Application-level `responseCode` values
- Required JSON keys and expected values
- Response messages
- JSON schema validation

The project handles an important API difference correctly. JSONPlaceholder behaves like a normal REST API, so tests validate `response.status_code`. Automation Exercise commonly returns HTTP `200` at the transport level even when the operation represents a `400`, `404`, or `405` result. Its tests therefore validate the `responseCode` value inside the JSON response body.

### Hooks and Reporting Layer

`features/environment.py` contains Behave hooks that:

1. Log the start and completion of the test run.
2. Create fresh API client instances before every scenario.
3. Reset the scenario response so state does not leak between scenarios.
4. Attach response URL, status, and body details to Allure after each step when Allure is available.
5. Record the final scenario status.

Allure stores raw execution results in `reports/allure-results/` and can generate a readable HTML report in `reports/allure-report/`.

## Concepts Demonstrated

This project demonstrates the following Python and test automation concepts:

- REST API testing
- HTTP methods: GET, POST, PUT, PATCH, and DELETE
- Request headers, parameters, JSON bodies, and form data
- Python classes, inheritance, and reusable methods
- `requests.Session` for consistent API communication
- Configuration through environment variables
- Behavior-Driven Development using Gherkin and Behave
- Feature files, scenarios, backgrounds, tags, and scenario outlines
- Positive, negative, and smoke test design
- Centralized assertions and response validation
- Logging and debugging of requests and responses
- Allure test reporting and evidence attachment
- Mocked HTTP testing without network access
- Separation of test behavior from framework implementation
- Extensible authentication helpers for future bearer-token APIs

## Applications and Practical Use

The framework can be applied to:

- Regression testing of REST APIs
- Validation of CRUD services
- Verification of positive and negative API behavior
- Smoke testing after a deployment
- Authentication and login endpoint testing
- Data-driven endpoint testing
- API contract and response-content checks
- Continuous integration test pipelines
- Training and demonstration of Python API automation
- Extending a test suite to new APIs and environments

Although the project uses public practice APIs, the same architecture can be adapted to internal development, staging, or production-like API environments by changing configuration values and adding endpoint-specific clients and feature files.

## Prerequisites

### Required Software

- Python 3.10 or later
- Internet access for live API tests
- A terminal or command prompt
- An editor such as Visual Studio Code

Java 8 or later is required only when using the Allure command-line tool to generate or open the HTML report. Java is not required to execute the Python or Behave tests.

### Python Dependencies

The dependencies are listed in `PROJECT_FOLDER/requirements.txt`:

- `requests` for HTTP communication
- `behave` for BDD test execution
- `allure-behave` for Allure integration
- `jsonschema` for schema validation helpers
- `python-dotenv` for environment-based configuration support
- `responses` for mocked offline HTTP tests

## Installation and Setup

Open a terminal in the project directory:

```bash
cd "2. Capestone_project/PROJECT_FOLDER"
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

On Windows:

```bash
.venv\Scripts\activate
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

Install the Python dependencies:

```bash
pip install -r requirements.txt
```

## Complete Workflow Methodology

The project follows this workflow from setup through reporting:

### Step 1: Define the Behavior

The required API behavior is written in a `.feature` file using Gherkin. Each scenario describes the request, expected response code, and expected response content.

### Step 2: Select the Test Scope

Behave tags identify the desired scope. For example, `@smoke` selects fast health-check scenarios, while `@negative` selects invalid-method, invalid-input, or missing-parameter behavior.

### Step 3: Initialize the Scenario

Before each scenario, Behave calls `before_scenario()` in `environment.py`. Fresh `UserManagementClient` and `AutomationExerciseClient` objects are attached to the scenario context, and the response state is reset.

### Step 4: Execute the Step Definition

Behave matches each Gherkin sentence to a Python function in `features/steps/`. The step function obtains the appropriate client and calls an endpoint-specific method.

### Step 5: Build and Send the Request

The endpoint-aware client chooses the endpoint constant and request format. The generic `APIClient` builds the complete URL, applies headers and timeout settings, sends the request through `requests.Session`, and logs the response.

### Step 6: Validate the Response

The step definition calls the appropriate reusable assertion:

- Check the actual HTTP status for JSONPlaceholder.
- Check the JSON body `responseCode` for Automation Exercise.
- Verify expected JSON fields, values, or response messages.

### Step 7: Capture Evidence

After each step, the Behave hook attaches the response URL, transport status, and response body to the Allure result when the Allure formatter is active.

### Step 8: Produce the Test Report

Behave displays the execution result in the terminal. Allure converts the raw results into an HTML report containing scenario status and request/response evidence.

### Step 9: Run the Offline Sanity Check When Needed

`tests_offline_smoke.py` uses the `responses` library to mock HTTP calls. It verifies the core API clients and assertion helpers without requiring access to the live APIs. This is useful for a restricted environment or a quick framework-level check, but it does not replace the live Behave suite.

## Project Structure

```text
2. Capestone_project/
├── Project_Description.md       # Detailed capstone documentation
├── Video_Presentation.md        # Space for project presentation details
└── PROJECT_FOLDER/
	├── .gitignore               # Ignored files and generated content
	├── README.md                # Project setup and usage guide
	├── requirements.txt         # Python dependencies
	├── behave.ini               # Behave execution configuration
	├── tests_offline_smoke.py   # Mocked HTTP sanity checks
	├── features/
	│   ├── environment.py       # Behave hooks and Allure attachments
	│   ├── user_management.feature
	│   ├── product_api.feature
	│   ├── search_product.feature
	│   ├── login_api.feature
	│   └── steps/
	│       ├── common_steps.py
	│       ├── login_steps.py
	│       ├── product_steps.py
	│       ├── search_steps.py
	│       └── user_steps.py
	├── framework/
	│   ├── __init__.py
	│   ├── api_client.py         # Generic and endpoint-aware API clients
	│   ├── auth.py               # Bearer-token helper functions
	│   ├── config.py             # URLs, timeout, headers, and credentials
	│   ├── endpoints.py          # Central endpoint path constants
	│   ├── logger.py             # Shared logging configuration
	│   └── utils.py              # Shared assertions and validation helpers
	├── test_data/
	│   ├── login_credentials.json
	│   ├── search_terms.json
	│   └── users.json
	├── reports/
	│   ├── allure-results/       # Generated raw Allure results
	│   └── allure-report/        # Generated HTML report
	└── .venv/                    # Local virtual environment
```

The `.venv/`, raw report files, and generated HTML report are environment or execution artifacts. They are created locally and should not be treated as application source code.

## How to Run the Tests

Run the complete Behave suite:

```bash
behave
```

Run one feature:

```bash
behave features/login_api.feature
```

Run tests by tag:

```bash
behave --tags=@smoke
behave --tags=@negative
behave --tags=@login,@negative
```

Verify that every Gherkin step has a matching Python step definition without making HTTP calls:

```bash
behave --dry-run
```

Run the offline mocked sanity check:

```bash
python tests_offline_smoke.py
```

## Allure Reporting

Generate raw Allure results:

```bash
behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results
```

Generate the HTML report:

```bash
allure generate reports/allure-results -o reports/allure-report --clean
```

Open the report locally:

```bash
allure open reports/allure-report
```

## Expected Outcome

After successful execution, the framework should:

- Discover all Behave feature files.
- Match Gherkin steps to Python definitions.
- Send requests to the configured APIs when network access is available.
- Validate HTTP or application-level response codes correctly.
- Verify expected JSON fields and response messages.
- Report passed and failed scenarios clearly.
- Attach response evidence to Allure results.
- Run the offline smoke checks independently with mocked responses.

## Extensibility and Future Improvements

The framework can be extended by:

1. Adding a new endpoint constants class in `framework/endpoints.py`.
2. Adding an endpoint-aware client in `framework/api_client.py`.
3. Adding reusable assertions to `framework/utils.py`.
4. Creating a new `.feature` file with tagged scenarios.
5. Adding matching step definitions under `features/steps/`.
6. Adding test data to `test_data/` when a scenario needs external fixtures.
7. Extending `framework/auth.py` for OAuth or JWT token flows.
8. Integrating Behave and Allure commands into a CI pipeline.

This design allows new API coverage to be added without duplicating request setup, configuration, logging, or validation logic.
