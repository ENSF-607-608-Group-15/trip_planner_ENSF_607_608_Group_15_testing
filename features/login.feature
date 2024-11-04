Feature: User Login functionality

  @test
  Scenario: User login with no credentials
    Given I got navigated to Signup page
    When I switch to Login view
    And I click Login button
    Then I should get an error message with text as "Please fill out this field."

  @login
  Scenario: User login with invalid credentials
    Given I got navigated to Signup page
    When I switch to Login view
    And I enter username as "UnregisteredUser"
    And I enter password as "fakepassword"
    And I click Login button
    Then I should get redirected to the Sign up page

  @login
  Scenario Outline: User login with valid credentials
    Given I got navigated to Signup page
    When I switch to Login view
    And I enter username as "<username>"
    And I enter password as "<password>"
    And I click Login button
    Then I should get logged in
    Examples:
    | username | password         |
    | a        | a                |
    | Poz      | awesomepassword  |
    | Neos     | this-is-garbage8 |
