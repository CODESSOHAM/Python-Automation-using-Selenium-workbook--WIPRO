Feature: Selenium Form Automation

  Scenario: Fill the automation practice form
    Given I open the automation practice website
    When I enter my name
    And I enter my email
    And I enter my phone number
    And I select the male gender
    Then the form data should be entered successfully
