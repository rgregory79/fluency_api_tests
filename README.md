# Fluency API Test Automation

This project contains automated tests for the "Account Management" section of Fluency's Customer Facing API. These tests are designed to validate the functionality, security, and performance of the API.

## Prerequisites

Before running the tests, make sure you have the following prerequisites:

- Python (3.x recommended) installed on your system.
- Install K6 for performance, load and stress testing
- Required Python libraries installed using `pip`:

  ```shell
  pip install -r requirements.txt

  k6 run k6_account_creation.js
  k6 run k6_unauthorized_access.js

## Link to Test Plan
- https://docs.google.com/document/d/1-xeslfYY5sho2O2JDUHPiisssb49muB27ugNIKmaGWA/edit?usp=sharing
