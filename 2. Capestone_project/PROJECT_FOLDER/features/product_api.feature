Feature: Products and Brands List API
  As a QA engineer
  I want to verify the products and brands list endpoints
  So that I can confirm correct methods are supported and rejected

  Background:
    Given the Automation Exercise API is available

  @smoke @products
  Scenario: Get all products list
    When I send a GET request to the products list endpoint
    Then the API response code should be 200
    And the response JSON should contain "products"

  @products @negative
  Scenario: POST to products list is not allowed
    When I send a POST request to the products list endpoint
    Then the API response code should be 405
    And the response message should contain "not supported"

  @smoke @brands
  Scenario: Get all brands list
    When I send a GET request to the brands list endpoint
    Then the API response code should be 200
    And the response JSON should contain "brands"

  @brands @negative
  Scenario: PUT to brands list is not allowed
    When I send a PUT request to the brands list endpoint
    Then the API response code should be 405
    And the response message should contain "not supported"
