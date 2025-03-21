# Created by alinakinziabaeva at 21.03.2025
Feature: Test scenarios for cart functionality


  Scenario: User can see an empty cart
    Given Open target page
    When Click on cart icon
    Then “Your cart is empty” message is shown
