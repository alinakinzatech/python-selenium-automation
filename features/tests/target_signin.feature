# Created by alinakinziabaeva at 21.03.2025
Feature: Sign In
  # Enter feature description here

  Scenario: Logged out user can navigate to Sign In
     Given Open target page
     When Click Sign In
     And From right side navigation menu, click Sign In
     Then Sign In form opened
    # Enter steps here