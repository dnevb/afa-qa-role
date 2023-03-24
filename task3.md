# Task #3: QA Testing plan

## Overview

Considering the app is using React Native the test environment will be in the source code, using a RN library like JEST, if not the case we can use the software Appium for testing similar as Selenium. The successful and failed tests will be stored and with that information create a pdf report and an email informing about the problems found

## Test cases

List of features with their test cases and the expected behavior of each one (emoji at the left)

- [ ] a. Will be tested if the app allow the user to create a reservation in an available date and hour.
  - ✅ 1. Check if show the correct hours between 6pm to 12am between monday and thurstday.
  - ✅ 2. Check if show the correct hours between 6pm to 2am between friday and sunday.
  - ❎ 3. Check if allow you to reservate more than 1 hours
  - ❎ 4. Check if allow you to create 21 reservations at the same day and time.
- [ ] b. Will be tested if the app calculate the correct amount of tip and totals
  - ❎ 1. Check if allow you to enter 27% of tip with a cost of 20 dollars
  - ❎ 2. Check if allow you to enter 0% of tip with a cost of 0 dollars
  - ✅ 3. Check if the total of the bill is 137.4 with 10% of tip with a cost of 60 dollars
