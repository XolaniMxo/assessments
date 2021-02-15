Feature: Universal Music Player

  Scenario: Navigate the Universal Music Player
    Given The Universal Music Player app is open
    When the user goes to the shop
    Then just arrived collections are shown
