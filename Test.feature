# Created by Matt at 11/24/2020
Feature: Retirement year specifically between 1900 and 1937
  This feature tells your retirement age if you were born
  between the year 1900 and 1937,
  which come to 65 and month 0.
  You can retire at age 65 and month 0 if born between those years.

  Scenario: calculate retirement age 65 year 0 month
    Given retirement age between 1900 and 1937
    When assert these values
    Then the value equals year 65 month 0