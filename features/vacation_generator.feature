Feature: Vacation generator functionality

  @vacation
  Scenario: [TC0014] User provides all mandatory vacation parameters
    Given I got navigated to Login page
    When I enter login username as "Neos"
    And I enter login password as "this-is-garbage8"
    And I click Login button
    And I enter departure city as "toronto"
    And I enter return date as "2024-11-30"
    And I enter departure date as "2024-11-25"
    And I enter desired trip location as "bangkok"
    And I enter a budget limit of "2500"
    And I enter a trip theme as "cafe"
    And I click Generate My Trip button
    Then I should see the vacation planning details

  @vacation
  Scenario: [TC0015] User views previous vacation plans
    Given I got navigated to Login page
    When I enter login username as "abc"
    And I enter login password as "123"
    And I click Login button
    And I click the Previous Vacation Plans button
    Then I should see a list of previously generated plans

  @vacation
  Scenario: [TC0016] User selects suggestion options
    Given I got navigated to Login page
    When I enter login username as "abc"
    And I enter login password as "123"
    And I click Login button
    And I enter departure city as "calgary"
    And I enter return date as "2024-11-30"
    And I enter departure date as "2024-11-25"
    And I enter desired trip location as "toronto"
    And I enter a budget limit of "2500"
    And I enter a trip theme as "museum"
    And I select the family-friendly option
    And I select the no-flying option
    And I select the disability-friendly option
    And I select the group discount option
    And I click Generate My Trip button
    Then I should see vacation plan suggestions related to "family,disability,group,discount"
    And I should see vacation plan suggestions not related to "fly,plane"

  @vacation
  Scenario: [TC0017] User enters negative value of budget
  Given I got navigated to Login page
    When I enter login username as "abc"
    And I enter login password as "123"
    And I click Login button
    And I enter a budget limit of "-2500"
    Then I should see an error popup indicating "Please enter a positive value."

  @vacation
  Scenario: [TC0018] User enters return date earlier than departure date
    Given I got navigated to Login page
    When I enter login username as "abc"
    And I enter login password as "123"
    And I click Login button
    And I enter departure city as "calgary"
    And I enter departure date as "2024-11-25"
    And I enter return date as "2024-11-02"
    And I click Generate My Trip button
    # Change to your date format
    Then I should get a return date error message with text as "Value must be 112520-02-04 or later." 

  @vacation
  Scenario: [TC0018] Version 2, User enter return date earlier than departure date
    Given I got navigated to Login page
    When I enter login username as "abc"
    And I enter login password as "123"
    And I click Login button
    And I enter departure city as "calgary"
    And I enter return date as "2024-11-02"
    And I enter departure date as "2024-11-25"
    Then I should see an error popup indicating "Return date cannot be earlier than departure date."
  
  @vacation
  Scenario: [TC0019] User sees presence of PDF download link
  Given I got navigated to Login page
    When I enter username as "abc"
    And I enter password as "123"
    And I click Login button
    And I enter departure city as "calgary"
    And I enter departure date as "2024-11-25"
    And I enter return date as "2024-11-30"
    And I enter desired trip location as "toronto"
    And I enter a budget limit of "2500"
    And I enter a trip theme as "museum"
    And I click Generate My Trip button
    Then I should see a PDF download link 
 
  @vacation
  Scenario: [TC0020] User skips required fields for trip planning
    Given I got navigated to Login page
    When I enter username as "abc"
    And I enter password as "123"
    And I click Login button
    And I click Generate My Trip button
    Then I should see required field error messages for each missing input