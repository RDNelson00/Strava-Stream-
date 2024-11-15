import requests
import os
import webbrowser
from urllib.parse import urlencode, urlparse, parse_qs
from dotenv import load_dotenv

# Load environment variables from .env file (client_id, client_secret, redirect_uri)
load_dotenv()

# Get your Strava API credentials from environment variables
client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
redirect_uri = os.getenv("redirect_URI")  # The URI to which Strava will redirect with the code
scope = os.getenv("scope")  # Modify as needed (example: read,activity:read)

# Step 1: Generate the authorization URL
def generate_auth_url():
    base_url = "https://www.strava.com/oauth/authorize"
    
    # Prepare the parameters
    params = {
        "client_id": client_id,
        "response_type": "code",  # Request an authorization code
        "redirect_uri": redirect_uri,
        "scope": scope,
    }
    
    # Construct the full URL
    auth_url = f"{base_url}?{urlencode(params)}"
    return auth_url





# Step 2: Redirect user to Strava authorization URL
def redirect_user_to_strava():
    auth_url = generate_auth_url()
    print("Opening browser for user authorization...")
    webbrowser.open(auth_url)  # Open the authorization URL in the default web browser

# Step 3: Handle the redirect from Strava (capture the authorization code)
def get_auth_code_from_redirect(url):
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    code = query_params.get("code")
    
    if code:
        return code[0]  # Return the first value of the 'code' parameter
    else:
        print("Error: Authorization code not found in the URL.")
        return None

# Step 4: Update the .env file with the authorization code
def update_env_file(key, value):
    # Wrap the value in double quotes
    value = f'"{value}"'
    
    # Read the existing .env content
    env_file_path = ".env"
    with open(env_file_path, "r") as file:
        lines = file.readlines()
    
    # Check if the key exists; if so, update it
    updated = False
    with open(env_file_path, "w") as file:
        for line in lines:
            if line.startswith(f"{key}="):
                file.write(f"{key}={value}\n")  
                updated = True
            else:
                file.write(line)
        
        # If the key wasn't found, append it
        if not updated:
            file.write(f"{key}={value}\n")
    print(f"Updated {key} in .env file.")


if __name__ == "__main__":
    redirect_user_to_strava()
    
    # Get the redirected URL from the user
    redirected_url = input("Paste the redirected URL here: ")
    auth_code = get_auth_code_from_redirect(redirected_url)
    
    if auth_code:
        print(f"Authorization code: {auth_code}")
        update_env_file("auth_code", auth_code)
    else:
        print("Failed to retrieve authorization code.")