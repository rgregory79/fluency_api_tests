import pytest
import requests

# Set the API endpoint for account update
API_URL = 'https://api.fluencyinc.co/account/update'

@pytest.mark.parametrize('update_data', [
    {'account_id': 123, 'contact_email': 'updated@example.com'},
    {'account_id': 456, 'contact_phone': '123-456-7890'},
])
def test_account_update(update_data):
    # Send a PUT request to update account information
    response = requests.put(API_URL, json=update_data)
    
    # Check if the response status code is 200 (OK)
    assert response.status_code == 200
    
    # TODO: Add more assertions to verify the response JSON or data as needed

# Add more test cases for account update as needed
