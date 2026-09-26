Feature: Verify Login API
  As a QA engineer
  I want to verify the login endpoint's behaviour
  So that valid, invalid, and malformed requests are all handled correctly

  Background:
    Given the Automation Exercise API is available

  @smoke @login
  Scenario: Login with valid email and password
    When I verify login with valid credentials
    Then the API response code should be 200
    And the response message should contain "User exists"

  @login @negative
  Scenario: Login without the email parameter
    When I verify login using only a password
    Then the API response code should be 400
    And the response message should contain "email or password parameter is missing"

  @login @negative
  Scenario: Login with invalid credentials
    When I verify login with invalid credentials
    Then the API response code should be 404
    And the response message should contain "User not found"

  @login @negative
  Scenario: DELETE to verify login is not allowed
    When I send a DELETE request to verify login
    Then the API response code should be 405
    And the response message should contain "not supported"
