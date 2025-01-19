import json
from datetime import datetime, timezone
import RefreshToken
import GetActivities
import GetAuthorization
import GetToken
import os
from dotenv import load_dotenv

# Load the environment variables
load_dotenv()

token_file = os.getenv('token_file')
auth_code = os.getenv("auth_code")  # Check for auth_code in .env

# Function to check if th e user has granted authorization
def is_authorized():
    return auth_code is not None
    

def get_token_expiry():
    try:
        with open(token_file, 'r') as f:
            tokens = json.load(f)
            return tokens.get('expires_at')  # Extract the refresh token
    except:         
        print("Token file not found. Getting tokens.")
        GetToken.main()

print(f"Auth code from environment: {os.getenv('auth_code')}")


# Main Logic
if not is_authorized():
    print("Authorization not found. Starting the authorization flow...")
    GetAuthorization.main()
    print("Starting token flow")
    GetToken.main()
    print("Fetching activities.")
    GetActivities.main()


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