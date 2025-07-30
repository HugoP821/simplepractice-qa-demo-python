Feature: Login to SimplePractice

  Scenario: Open homepage
    Given I open the browser
    When I navigate to the homepage
    Then the page title should contain "SimplePractice"