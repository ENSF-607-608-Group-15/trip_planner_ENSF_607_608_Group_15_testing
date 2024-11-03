Feature: User Login functionality

  @login
  Scenario: User login with no credentials
    Given I got navigated to Login page
    When I click Login button
    Then I should get an error message with text as "Incorrect password!"

  @login
  Scenario: User login with invalid credentials
    Given I got navigated to Login page
    When I enter username as "UnregisteredUser"
    And I enter password as "fakepassword"
    And I click Login button
    Then I should get an error message with text as "Incorrect password!"

  @login
  Scenario Outline: User login with valid credentials
    Given I got navigated to Login page
    When I enter username as "<username>"
    And I enter password as "<password>"
    And I click Login button
    Then I should get logged in
    Examples:
    | username   | password     |
    | test       | testpassword |
    | test123    | testpassword |
    | test430945 | testPW123    |
