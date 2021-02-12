@Login
Feature: Login

  Scenario: Positive User Credentials
    Given the home page is open
    When the user logs in with username "tomsmith" and password "SuperSecretPassword!"
    And the message "You logged into a secure area!" is shown
    Then the user logs out

  Scenario: Wrong Username
    Given the home page is open
    When the user logs in with username "wrongUserName" and password "SuperSecretPassword!"
    Then the error message "Your username is invalid!" is shown

  Scenario: Wrong Password
    Given the home page is open
    When the user logs in with username "tomsmith" and password "wrongPassword!"
    Then the message "Your password is invalid!" is shown