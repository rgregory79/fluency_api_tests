import pytest
import requests

# Set the API endpoint for account creation
API_URL = 'https://api.fluencyinc.co/account/create'

@pytest.mark.parametrize('account_data', [
    {'account_name': 'TestAccount1', 'contact_email': 'rob.gregory79@yahoo.com'},
    {'account_name': 'TestAccount2', 'contact_email': 'test2@example.com'},
])
def test_account_creation(account_data):
    # Send a POST request to create an account
    response = requests.post(API_URL, json=account_data)
    
    # Check if the response status code is 200 (OK)
    assert response.status_code == 200
    
    # TODO: Add more assertions to verify the response JSON 

@pytest.mark.parametrize('invalid_account_data', [
    {'account_name': '', 'contact_email': 'test@example.com'},
    {'account_name': 'TestAccount3', 'contact_email': ''},
])
def test_invalid_account_creation(invalid_account_data):
    # Send a POST request with invalid data
    response = requests.post(API_URL, json=invalid_account_data)
    
    # Check if the response status code is 4xx (Client Error)
    assert response.status_code >= 400

# Add more test cases as needed
