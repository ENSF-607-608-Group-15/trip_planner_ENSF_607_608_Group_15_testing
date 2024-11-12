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

  @vacation @previous_plans
  Scenario: [TC0015] User views previous vacation plans
    Given I got navigated to Login page
    When I enter login username as "abc"
    And I enter login password as "123"
    And I click Login button
    And I click the Previous Vacation Plans button
    Then I should see a list of previously generated plans

  @vacation @trip_options
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
    Then I should see vacation plan suggestions related to "family, disability, group, discount"
    And I should see vacation plan suggestions not related to "fly, plane"

  @vacation @trip_budget @error_message
  Scenario: [TC0017] User enters negative value of budget
  Given I got navigated to Login page
    When I enter login username as "abc"
    And I enter login password as "123"
    And I click Login button
    And I enter a budget limit of "-2500"
    Then I should see an error popup indicating "Please enter a positive value."

  @vacation @error_message
  Scenario: [TC0018] User enters return date earlier than departure date
    Given I got navigated to Login page
    When I enter login username as "abc"
    And I enter login password as "123"
    And I click Login button
    And I enter departure city as "calgary"
    And I enter return date as "2024-11-02"
    And I enter departure date as "2024-11-25"
    Then I should see an error popup indicating "Return date cannot be earlier than departure date."
  
  @vacation @pdf_export
  Scenario: [TC0019] User sees presence of PDF download link
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
    And I click Generate My Trip button
    Then I should see a PDF download link 
 
  @vacation @error_message
  Scenario: [TC0020] User skips required fields for trip planning
    Given I got navigated to Login page
    When I enter login username as "abc"
    And I enter login password as "123"
    And I click Login button
    And I click Generate My Trip button
    Then I should see required field error messages for inputs "Departure City, Desired Trip Location"

  @vacation @previous_vacation_settings
  Scenario: [TC0021] User views previous trip settings
    Given I got navigated to Login page
    When I switch to Sign up view
    And I enter sign up username as random_username
    And I enter sign up password as random_password
    And I click Sign up button
    Then I should be navigated to the Login page
    When I enter login username
    And I enter login password
    And I click Login button
    And I click Generate My Trip button
    And I enter departure city as "calgary"
    And I enter return date as "2025-10-25"
    And I enter departure date as "2025-10-11"
    And I enter desired trip location as "toronto"
    And I enter a budget limit of "2500"
    And I enter a trip theme as "cafe"
    And I select the disability-friendly option
    And I select the group discount option
    And I click Generate My Trip button
    And I click the Previous Settings button
    Then I should see a table of my previous trip settings containing "2025-10-11, 2025-10-25, calgary, cafe, toronto, $2500.0, No No Yes Yes"
