Feature: Test the functionality of the login

    Scenario: Check that No customer account found message appears when introducing an unregistred email
      Given I am on the Login page of https://demo.nopcommerce.com/login
      When I insert an unregistered email field
      And  I insert the password
      And I click on login button
      Then I get the following message 'Login was unsuccesful'

"""
Dupa proiectul sustinut online

Feature: Test the functionality of the login
  Scenario: Check that "No customer account found" message appears when introducing an unregistered email
    Given I am on the login page https://demo.nopcommerce.com/login
    When I insert an unregistered email in the email field
    And I insert a password
    And I click on login button
    Then I get the following message Login was unsuccessful. Please correct the errors and try again. No customer account found


"""