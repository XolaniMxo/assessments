@MusicPlayer
Feature: Navigate Universal Music player

  Scenario: Navigate Universal Music player and play a song
    Given the menu is open
     When the user goes to genres
     And the user chooses Rock
	 Then the user plays Awakening and closes the application