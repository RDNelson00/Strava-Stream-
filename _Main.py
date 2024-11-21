import json
from datetime import datetime, timezone
import RefreshToken
import GetActivities
import GetAuthorization
import GetToken


import os


token_file = 'strava_tokens.json'

# Function to check if the user has granted authorization
def is_authorized():
    auth_code = os.getenv("auth_code")  # Check for auth_code in .env
    return auth_code is not None

def get_token_expiry():
    with open(token_file, 'r') as f:
        tokens = json.load(f)
        return tokens.get('expires_at')  # Extract the refresh token
        



# Main Logic
if not is_authorized():
    print("Authorization not found. Starting the authorization flow...")
    GetAuthorization.main()  
else:
    print("Authorization found. Checking token status...")

    # Check token expiry
    expiry = get_token_expiry()
    if expiry:
        expiry = datetime.fromtimestamp(expiry, tz=timezone.utc)  # Convert to UTC
        print("Access token expires at", expiry, ". Right now it is", datetime.now(timezone.utc))

        # Refresh the token if expired
        if expiry < datetime.now(timezone.utc):
            print("Token is expired. Refreshing...")
            RefreshToken.main()
            GetActivities.main() 
  
        else:
            print("Token is valid. Fetching activities...")
            GetActivities.main() 
    else:
        print("Token file not found or invalid. Starting the authorization flow...")
        GetAuthorization.main()