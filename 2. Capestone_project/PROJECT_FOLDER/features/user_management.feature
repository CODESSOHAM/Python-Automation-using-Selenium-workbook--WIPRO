Feature: User Management API
  As an API consumer
  I want to create, read, update, and delete users
  So that I can manage user records via the jsonplaceholder service

  Background:
    Given the User Management API is available

  @smoke @users
  Scenario: Get all users
    When I request all users
    Then the response code should be 200
    And the response should contain a list of users

  @users
  Scenario: Get a single user by ID
    When I request the user with id 1
    Then the response code should be 200
    And the user response should contain field "id" with value 1

  @users
  Scenario: Create a new user
    When I create a new user with the sample payload
    Then the response code should be 201
    And the user response should contain field "name" with value "Jane Doe"

  @users
  Scenario: Update an existing user
    When I update user 1 with the updated payload
    Then the response code should be 200
    And the user response should contain field "name" with value "Jane D. Smith"

  @users
  Scenario: Delete a user
    When I delete user 1
    Then the response code should be 200

  @users @negative
  Scenario: Get a user that does not exist
    When I request the user with id 99999
    Then the response code should be 404
