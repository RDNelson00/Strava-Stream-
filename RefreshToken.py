import requests
import pandas as pd
import time
import json  # Import json for reading/writing JSON files
from GetToken import load_env_variables

# File to store the access token and refresh token



def get_refresh_token():
    token_file = "strava_tokens.json"
    with open(token_file, 'r') as f:
        tokens = json.load(f)
        refresh_token = tokens.get('refresh_token')  # Extract the refresh token
        return refresh_token, token_file


# Get the new access token using the refresh token
def get_token(refresh_token, token_file):
    
    client_id, client_secret, auth_code = load_env_variables()

    # Endpoint for refreshing the token
    token_url = "https://www.strava.com/oauth/token"
    
    # Payload with credentials and refresh token
    payload = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': "refresh_token",
        'refresh_token':   refresh_token
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


def main():
    
    #load the refresh token from the token file
    refresh_token, token_file = get_refresh_token()

    #retreive the new token
    get_token(refresh_token, token_file)


if __name__ == "__main__":
    main()