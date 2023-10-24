import pytest
import requests

# Set the API endpoint for account creation
API_URL = 'https://api.fluencyinc.co/account/create'

@pytest.mark.parametrize('account_data', [
    {'account_name': 'TestAccount1', 'contact_email': 'test1@example.com'},
    {'account_name': 'TestAccount2', 'contact_email': 'test2@example.com'},
])
def test_duplicate_account_creation(account_data):
    # Create an account with valid data
    response = requests.post(API_URL, json=account_data)
    
    # Check if the response status code is 200 (OK)
    assert response.status_code == 200
    
    # Attempt to create the same account again
    response = requests.post(API_URL, json=account_data)
    
    # Check if the response status code is 4xx (Client Error) indicating duplicate creation
    assert response.status_code >= 400

# Add more test cases for duplicate account creation as needed
