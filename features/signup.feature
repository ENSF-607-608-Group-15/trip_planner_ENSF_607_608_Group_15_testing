Feature: User Sign up functionality

  @signup
  Scenario: [TC0001] User sign up basic workflow
    Given I got navigated to Login page
    When I switch to Sign up view
    Then I should be navigated to the Sign up page
    When I enter sign up username as random_username
    And I enter sign up password as random_password
    And I click Sign up button
    Then I should be navigated to the Login page
    When I enter login username
    And I enter login password
    And I click Login button
    Then I should get logged in

  @signup @error_message
  Scenario: [TC0002] User sign up with taken username
    Given I got navigated to Login page
    When I switch to Sign up view
    And I enter sign up username as "taken_username"
    And I enter sign up password as "my_password"
    And I click Sign up button
    Then I should get a sign up error message with text as "Please enter a valid username and password."

  @signup @error_message
  Scenario Outline: [TC0003] User sign up with username or password containing whitespaces
    Given I got navigated to Login page
    When I switch to Sign up view
    And I enter sign up username as "<username>"
    And I enter sign up password as "<password>"
    And I click Sign up button
    Then I should get a sign up error message with text as "Username and password cannot contain whitespaces."
    Examples:
      | username | password     |
      | bad user | goodpassword |
      | gooduser | bad password |
      | bad user | bad password |

  @signup
  Scenario: [TC0004] User sign up with blank username
    Given I got navigated to Login page
    When I switch to Sign up view
    And I enter sign up password as random_password
    And I click Sign up button
    Then I should get a sign up username error message with text as "Please fill out this field."

  @signup
  Scenario: [TC0005] User sign up with blank password
    Given I got navigated to Login page
    When I switch to Sign up view
    And I enter sign up username as random_username
    And I click Sign up button
    Then I should get a sign up password error message with text as "Please fill out this field."
