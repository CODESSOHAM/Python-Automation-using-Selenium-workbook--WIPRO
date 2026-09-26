Feature: Search Product API
  As a QA engineer
  I want to verify the search product endpoint
  So that valid searches succeed and invalid ones fail predictably

  Background:
    Given the Automation Exercise API is available

  @smoke @search
  Scenario Outline: Search for a product with a valid term
    When I search for the product "<term>"
    Then the API response code should be 200
    And the response JSON should contain "products"

    Examples:
      | term    |
      | top     |
      | tshirt  |
      | jean    |

  @search @negative
  Scenario: Search without the search_product parameter
    When I search for a product without providing the search term
    Then the API response code should be 400
    And the response message should contain "search_product parameter is missing"
