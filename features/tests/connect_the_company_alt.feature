# Created by alberthembd at 3/14/24
Feature: The user can connect his company to the service from the main page

  Scenario: Connect the company
    Given the user has logged into the main page
    When the user has Clicked on Connect the company in the left panel
    Then a new tab opens with a form to register his company