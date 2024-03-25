# Created by alberthembd at 3/12/24
Feature: The user is able to log into the Reely application
  and see that it has the basic functionality for viewing
  real estate properties in Bali.

  Scenario: The user can log into Really and view properties by cost,
  construction date, property type and location.
    Given that the user has logged into the main page
    When the user clicks Bali
    Then properties in Bali which are in the system will appear
#    When the user chooses construction date of 4Q 2024
#    Then properties that will have been completed prior to 4Q 2024 will appear
#    When the user selects value ranges from 600000 AED to 1.5 million AED
#    Then properties in Bali within that value range will appear
#    When the user selects property type of 'Apartment'
#    Then apartments will appear
#    When the user chooses 'Penthouse'
#    Then penthouses will appear

