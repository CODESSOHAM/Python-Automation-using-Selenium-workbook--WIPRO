Feature: Selenium POM Form Automation

  Scenario: Fill the automation practice form using POM
    Given I open the automation practice website
    When I enter my name through the POM
    And I enter my email through the POM
    And I enter my phone number through the POM
    And I select male gender through the POM
    Then the form details should be displayed correctly
