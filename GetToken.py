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
def get_token():
    global auth_code

    # Endpoint for refreshing the token
    token_url = "https://www.strava.com/oauth/token"
    
    # Payload with credentials and refresh token
    payload = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': "authorization_code",
        'code': auth_code  
    }
    
    # Make the POST request to refresh the token
    response = requests.post(token_url, data=payload)
    data = response.json()
    print("Response status code:", response.status_code)  # Print response code
    print("Response JSON data:", data)                    # Print response JSON data

    # Check if request was successful
    if response.status_code == 200:
        # Update the tokens and save them
        access_token = data['access_token']
       
        # Add the current time as issued_at
        issued_at = int(time.time())  # Get the current Unix timestamp

        # Add issued_at to the data
        data['issued_at'] = issued_at

        # Save the tokens as JSON
        with open(token_file, 'w') as f:
            json.dump(data, f)  # Correctly save data in JSON format
        return access_token
    else:
        raise Exception("Failed to refresh token:", data)

# get the access token
get_token()
