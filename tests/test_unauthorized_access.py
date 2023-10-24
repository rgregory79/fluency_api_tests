import pytest
import requests

# Set the API endpoint for unauthorized access
UNAUTHORIZED_API_URL = 'https://api.fluencyinc.co/unauthorized_endpoint'

def test_unauthorized_access():
    # Attempt to access an unauthorized endpoint
    response = requests.get(UNAUTHORIZED_API_URL)
    
    # Check if the response status code is 4xx (Client Error) indicating unauthorized access
    assert response.status_code >= 400

# Add more test cases for unauthorized access as needed
