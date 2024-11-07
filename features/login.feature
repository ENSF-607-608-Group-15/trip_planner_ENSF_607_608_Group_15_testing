Feature: User Login functionality

  @login
  Scenario: [TC0010] User login with no credentials
    Given I got navigated to Login page
    When I click Login button
    Then I should get a username error message with text as "Please fill out this field."

  @login
  Scenario: [TC0011] User login with invalid credentials
    Given I got navigated to Login page
    When I enter username as "UnregisteredUser"
    And I enter password as "fakepassword"
    And I click Login button
    Then I should get redirected to the Sign up page

  @login
  Scenario:[TC0012]  User login with valid credentials
    Given I got navigated to Login page
    When I enter username as "<username>"
    And I enter password as "<password>"
    And I click Login button
    Then I should get logged in
    Examples:
    | username | password         |
    | a        | a                |
    | Poz      | awesomepassword  |
    | Neos     | this-is-garbage8 |
