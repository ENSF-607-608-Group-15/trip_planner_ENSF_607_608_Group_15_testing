Feature: User Login functionality

  @login @error_message
  Scenario: [TC0006] User login with no credentials
    Given I got navigated to Login page
    When I click Login button
    Then I should get a login username error message with text as "Please fill out this field."

  @login @error_message
  Scenario: [TC0007] User login with invalid credentials
    Given I got navigated to Login page
    When I enter login username as "UnregisteredUser"
    And I enter login password as "fakepassword"
    And I click Login button
    Then I should get a login error message with text as "Invalid username or password. Please try again."

  @login
  Scenario Outline:[TC0008]  User login with valid credentials
    Given I got navigated to Login page
    When I enter login username as "<username>"
    And I enter login password as "<password>"
    And I click Login button
    Then I should get logged in
    Examples:
      | username | password         |
      | a        | a                |
      | Poz      | awesomepassword  |
      | Neos     | this-is-garbage8 |

  @login
  Scenario: [TC0009] Guest user login
    Given I got navigated to Login page
    When I click Continue as Guest button
    Then I should get logged in
