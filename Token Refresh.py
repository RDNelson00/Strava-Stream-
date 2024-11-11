import requests
import pandas as pd
import time
import os
import json  # Import json for reading/writing JSON files
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()


client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
auth_code = os.getenv("auth_code")

if not client_id or not client_secret or not auth_code:
    raise Exception("Missing one or more required environment variables.")

# File to store the access token and refresh token
token_file = "strava_tokens.json"

# Refresh token function
def refresh_access_token():
    global auth_code

    # Endpoint for refreshing the token
    token_url = "https://www.strava.com/oauth/token"
    
    # Payload with credentials and refresh token
    payload = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': "authorization_code"
        ,'auth_code': auth_code
    }

    # Make the POST request to refresh the token
    response = requests.post(token_url, data=payload)
    data = response.json()

    # Check if request was successful
    if response.status_code == 200:
        # Update the tokens and save them
        access_token = data['access_token']
        auth_code = data['auth_code']
        
        # Save the tokens as JSON
        with open(token_file, 'w') as f:
            json.dump(data, f)  # Correctly save data in JSON format

        return access_token
    else:
        raise Exception("Failed to refresh token:", data)

# Function to fetch activities
def fetch_activities():
    # Try loading the last saved access token
    try:
        with open(token_file) as f:
            tokens = json.load(f)
            access_token = tokens.get('access_token')
            # Additional code to use the access_token to fetch activities would go here
            
    except FileNotFoundError:
        print("Token file not found. Refreshing access token.")
        access_token = refresh_access_token()
    
    # Placeholder for making requests to fetch activities with access_token
    print("Access token:", access_token)

