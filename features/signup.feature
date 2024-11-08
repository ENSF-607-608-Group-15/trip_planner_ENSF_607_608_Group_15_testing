Feature: User Sign up functionality

  @signup
  Scenario: [TC0001] User sign up with username and password
    Given I got navigated to Login page
    When I click Sign up button
    Then I should be navigated to the Sign up page
    When  I enter username as random_username
    And I enter password as random_password
    And I click Sign up botton
    Then I should be navigated to the Login page

  @signup
  Scenario: [TC0002] User try to sign up with an already taken username
    Given I got navigated to Login page
    When I click Sign up button
    Then I should be navigated to the Sign up page
    When I enter username as "taken_username"
    And I enter password as "123"
    And I click Sign up botton
    Then I should get an error message with text as "Username is already taken"

  @signup
  Scenario: [TC0003] User sign up with empty username
    Given I got navigated to Login page
    When I click Sign up button
    Then I should be navigated to the Sign up page
    And I enter username as " "
    And I enter password as random_password
    Then I should get a username error message with text as "Please fill out this field."

  @signup
  Scenario: [TC0004] User sign up with empty password
    Given I got navigated to Login page
    When I click Sign up button
    Then I should be navigated to the Sign up page
    And I enter username as random_username
    And I enter password as " "
    Then I should get a password error message with text as "Please fill out this field."

  @signup
  Scenario: [TC0005] User sign up with empty username and empty password
    Given I got navigated to Login page
    When I click Sign up button
    Then I should be navigated to the Sign up page
    And I enter username as " "
    And I enter password as " "
    Then I should get a username error message with text as "Please fill out this field."
 