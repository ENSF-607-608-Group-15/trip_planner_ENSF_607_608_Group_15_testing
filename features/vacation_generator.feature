Feature: Vacation generator functionality

  Background:
    Given I got navigated to Login page

  @test
  Scenario: User provides all mandatory vacation parameters
    When I click Continue as Guest button
    Then I should be navigated to the main page
    When I enter departure city as "toronto"
    And I enter departure date as "0020241122"
    And I enter return date as "0020241130"
    And I enter desired trip location as "bangkok"
    And I enter a budget limit of "2500"
    And I click Generate My Trip button
    Then I should see the vacation planning details

  @vacation
  Scenario: User views previous vacation plans
    When I enter username as "abc"
    And I enter password as "123"
    And I click Login button
    Then I should be navigated to the main page
    When I click the Previous Vacation Plans button
    Then I should see a list of previously generated plans

  @family
  Scenario: User selects family-friendly option
    When I click Continue as Guest button
    Then I should be navigated to the main page
    When I enter departure city as "<departure_city>"
    And I enter departure date as "<departure_date>"
    And I enter return date as "<return_date>"
    And I enter desired trip location as "<desired_location>"
    And I enter a budget limit of "<budget>"
    And I select the family-friendly option
    Then I should see family-friendly vacation suggestions

  
