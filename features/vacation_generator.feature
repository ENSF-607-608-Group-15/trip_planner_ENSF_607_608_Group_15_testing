Feature: Vacation generator functionality

  @vacation
  Scenario: [TC0013] User provides all mandatory vacation parameters
    Given I got navigated to Login page
    When I enter login username as "Neos"
    And I enter login password as "this-is-garbage8"
    And I click Login button
    And I enter departure city as "toronto"
    And I enter departure date as "2024-11-20"
    And I enter return date as "2024-11-25"
    And I enter desired trip location as "bangkok"
    And I enter a budget limit of "2500"
    And I enter a theme as "cafe"
    And I click Generate My Trip button
    Then I should see the vacation planning details

  @vacation
  Scenario: [TC0014] User views previous vacation plans
    Given I got navigated to Login page
    When I enter username as "abc"
    And I enter password as "123"
    And I click Login button
    And I click the Previous Vacation Plans button
    Then I should see a list of previously generated plans

  @vacation
  Scenario: [TC0015] User selects suggestion options
    Given I got navigated to Login page
    When I enter username as "abc"
    And I enter password as "123"
    And I click Login button
    And I enter departure city as "calgary"
    And I enter departure date as "2024-11-11"
    And I enter return date as "2024-11-18"
    And I enter desired trip location as "toronto"
    And I enter a budget limit of "2500"
    And I enter a theme as "museum"
    And I select the family-friendly option
    And I select the no-flying option
    And I select the disability-friendly option
    And I select the group discount option
    And I click Generate My Trip button
    Then I should see vacation plan suggestions related to "family-friendly, train, disability-friendly, group discount"

  
