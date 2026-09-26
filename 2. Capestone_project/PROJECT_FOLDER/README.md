# API Automation Framework — Requests + Behave BDD + Allure

A reusable Python API test framework covering:
- **jsonplaceholder.typicode.com** — User Management CRUD (`/users`)
- **automationexercise.com/api** — Products, Brands, Search Product, Verify Login

Built with `requests`, `behave` (BDD/Gherkin), and `allure-behave` reporting.

## 1. Prerequisites

- Python 3.10+
- Internet access to `jsonplaceholder.typicode.com` and `automationexercise.com`
- Java 8+ (only needed to run the Allure **command-line report viewer**, not for running tests)

## 2. Setup

```bash
# 1. Clone / unzip the project, then cd into it
cd api-automation-framework

# 2. Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

Install the Allure CLI (only needed to view the pretty HTML report):

```bash
# macOS
brew install allure

# Linux (manual)
curl -o allure.zip -Ls https://github.com/allure-framework/allure2/releases/latest/download/allure-2.29.0.zip
unzip allure.zip -d /opt/ && sudo ln -s /opt/allure-2.29.0/bin/allure /usr/local/bin/allure

# Windows (scoop)
scoop install allure
```

## 3. Project Structure

```
api-automation-framework/
├── features/
│   ├── environment.py          # Behave hooks (client setup, Allure attachments)
│   ├── user_management.feature # jsonplaceholder /users CRUD scenarios
│   ├── product_api.feature     # productsList / brandsList scenarios
│   ├── search_product.feature  # searchProduct scenarios
│   ├── login_api.feature       # verifyLogin scenarios
│   └── steps/                  # Step definitions (Python) per feature
├── framework/
│   ├── api_client.py           # Generic requests wrapper + endpoint-aware clients
│   ├── endpoints.py            # All endpoint path constants
│   ├── config.py                # Base URLs, timeouts, env-var overrides
│   ├── auth.py                  # Auth/token helpers
│   ├── utils.py                 # Reusable assertion helpers
│   └── logger.py                # Consistent logging
├── test_data/                   # JSON fixtures (users, credentials, search terms)
├── reports/
│   ├── allure-results/          # Raw results (generated per run)
│   └── allure-report/           # Final HTML report (generated on demand)
├── tests_offline_smoke.py       # Optional: mocked HTTP sanity check, no network needed
├── requirements.txt
├── behave.ini
└── README.md
```

## 4. Running the Tests

### Run everything (plain console output)

```bash
behave
```

### Run a single feature

```bash
behave features/login_api.feature
```

### Run by tag (e.g. only smoke tests, or only negative tests)

```bash
behave --tags=@smoke
behave --tags=@negative
behave --tags=@login,@negative     # combine tags
```

### Dry-run (verify all Gherkin steps have matching step definitions, no HTTP calls made)

```bash
behave --dry-run
```

## 5. Generating the Allure Report

Behave doesn't know about Allure until you point it at the formatter:

```bash
# 1. Run tests and write raw Allure results
behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results

# 2. Generate the static HTML report from those results
allure generate reports/allure-results -o reports/allure-report --clean

# 3. Open it in a browser
allure open reports/allure-report
```

`allure open` starts a small local server and opens the report automatically.
Each scenario in the report will show the request/response details attached
by `features/environment.py`.

## 6. Offline Sanity Check (no network required)

If you want to confirm the framework's client and assertion logic works
without hitting the live APIs (useful in a restricted CI sandbox), run:

```bash
python tests_offline_smoke.py
```

This uses the `responses` library to mock HTTP calls and exercises every
client method + assertion helper. It is **not** a substitute for the real
Behave suite — run `behave` on a machine with internet access for the actual
capstone deliverable.

## 7. Configuration

Override defaults via environment variables (see `framework/config.py`):

```bash
export JSONPLACEHOLDER_BASE_URL="https://jsonplaceholder.typicode.com"
export AUTOMATIONEXERCISE_BASE_URL="https://automationexercise.com/api"
export API_TIMEOUT=20
export TEST_USER_EMAIL="you@example.com"
export TEST_USER_PASSWORD="yourpassword"
```

## 8. Extending the Framework

- **New API?** Add a `<Name>Endpoints` class in `endpoints.py`, a `<Name>Client(APIClient)`
  in `api_client.py`, a base URL in `config.py`, then write `.feature` files + steps.
- **New assertion?** Add it to `framework/utils.py` so it's reusable across step files.
- **Real authentication?** Extend `framework/auth.py` (e.g. token retrieval + injecting
  `Authorization` headers into `APIClient`'s session).

## 9. Important quirk: Automation Exercise always returns HTTP 200

**This API does not use real HTTP status codes for errors.** Every response —
success or failure — comes back with a transport-level HTTP 200. The actual
result is reported inside the JSON body, in a field called `responseCode`
(e.g. `{"responseCode": 405, "message": "This request method is not supported."}`).

This is a well-known behaviour of this specific practice API (confirmed by
several independent test frameworks built against it), not a bug in our
framework. Because of this:

- `features/user_management.feature` (jsonplaceholder) asserts on the **real
  HTTP status code** using the step `Then the response code should be X`,
  backed by `assert_status_code()` in `framework/utils.py` — jsonplaceholder
  behaves like a normal REST API.
- `features/product_api.feature`, `features/search_product.feature`, and
  `features/login_api.feature` (automationexercise) instead use
  `Then the API response code should be X`, backed by `assert_api_response_code()`,
  which opens the JSON body and checks the `responseCode` field. Asserting
  only on `response.status_code` here would make every "failure" test pass
  incorrectly, since the transport status is always 200.

If you extend this framework to a new endpoint, check which behaviour it
follows before picking a status-check step.

## 10. Expected response codes for the Automation Exercise API

Per the official API list (`automationexercise.com/api_list`), these are the
`responseCode` values inside the JSON body (not the HTTP status, which is
always 200 — see section 9):

| Endpoint                  | Method | Expected `responseCode` | Notes                              |
|----------------------------|--------|--------------------------|-------------------------------------|
| `/productsList`            | GET    | 200                      | Returns products list               |
| `/productsList`            | POST   | 405                      | Method not supported                |
| `/brandsList`               | GET    | 200                      | Returns brands list                 |
| `/brandsList`               | PUT    | 405                      | Method not supported                |
| `/searchProduct`            | POST   | 200                      | Requires `search_product` param     |
| `/searchProduct`            | POST   | 400                      | Missing `search_product` param      |
| `/verifyLogin`              | POST   | 200                      | Valid credentials → "User exists!"  |
| `/verifyLogin`              | POST   | 400                      | Missing email/password              |
| `/verifyLogin`              | POST   | 404                      | Invalid credentials → "User not found!" |
| `/verifyLogin`              | DELETE | 405                      | Method not supported                |
