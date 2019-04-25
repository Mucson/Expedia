# Created by Vladimir at 4/17/2019
Feature: booking
  booking fly ticket

  Background:
    Given I open main page

  Scenario: book_steps
    When I select Flights
    Then I type London in Flying from field and select Heatrow
    Then I type Dublin in Flying to field and select Dublin
    Then Select Returning: 12/07/2019
    Then Select Departing: 12/01/2019
    Then I pick two adult
    Then I click search button
    Then Assert that the price in first row is $116
    Then Assert that the first price is not $1
    Then Assert the visible list of “Airlines included” beneath the list of “Stops”