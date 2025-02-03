import json
from datetime import datetime, timezone
import StravaStream.RefreshToken
import  StravaStream.GetActivities
import  StravaStream.GetAuthorization
import  StravaStream.GetToken
import os
from dotenv import load_dotenv
import sys
import os

# Add the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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
        StravaStream.GetToken.main()

print(f"Auth code from environment: {os.getenv('auth_code')}")


# Main Logic
if not is_authorized():
    print("Authorization not found. Starting the authorization flow...")
    StravaStream.GetAuthorization.main()
    print("Starting token flow")
    StravaStream.GetToken.main()
    print("Fetching activities.")
    StravaStream.GetActivities.main()


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
            StravaStream.RefreshToken.main()
            StravaStream.GetActivities.main() 
  
        else:
            print("Token is valid. Fetching activities...")
            StravaStream.GetActivities.main() 
    else:
        print("Token file not found or invalid. Starting the authorization flow...")
        StravaStream.GetAuthorization.main()