Feature: register
  Scenario: register
    Given prepare to register
    When input valid data
    Then success register
