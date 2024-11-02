Feature: User Login functionality

  @login
  Scenario: User login with no credentials
    Given I got navigated to Login page
    When I click Login button
    Then I should get an error message with text as "Incorrect password!"

  @login
  Scenario: User login with invalid credentials
    Given I got navigated to Login page
    When I enter password as "555"
    And I click Login button
    Then I should get an error message with text as "Incorrect password!"

  @another
  Scenario: User login with valid credentials
    Given I got navigated to Login page
    When I enter password as "123"
    And I click Login button
    Then I should get logged in