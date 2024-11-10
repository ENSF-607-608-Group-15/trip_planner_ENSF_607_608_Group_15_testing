Feature: Vacation Planner functionality

  @plan_vacation
  Scenario:[TC0012] Plan vacation basic workflow
    Given I got navigated to Login page
    When I enter login username as "Neos"
    And I enter login password as "this-is-garbage8"
    And I click Login button
    And I enter a departure date as "2024-11-20"
