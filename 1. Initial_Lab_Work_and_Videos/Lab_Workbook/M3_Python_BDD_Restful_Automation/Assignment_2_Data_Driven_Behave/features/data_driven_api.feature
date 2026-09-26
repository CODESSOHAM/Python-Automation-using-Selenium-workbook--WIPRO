Feature: Data Driven API Testing

  Scenario: Validate multiple API posts using external test data
    Given I load the API test data
    When I send GET requests for all post IDs
    Then all API responses should have status code 200
