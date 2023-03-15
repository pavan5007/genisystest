Feature:
  User Login into application and select plan

  Scenario: Login and select plan
    Given I am on login screen
    And Log in to application
    When I go to the Library
    And I choose unlock access select plan
    Then I should be on plan demo
