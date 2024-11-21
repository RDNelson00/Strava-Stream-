import os
import webbrowser
from urllib.parse import urlencode, urlparse, parse_qs
from dotenv import load_dotenv

#first go get the parameters from the env var file
def build_params():
    """
    Load required environment variables for the Strava OAuth flow.
    Returns:
        client_id, redirect_uri, scope (tuple of strings)
    Raises:
        ValueError if any required environment variable is missing.
    """
    load_dotenv()
    
    
        
    client_id = os.getenv("client_id")
    redirect_uri = os.getenv("redirect_URI")
    scope = os.getenv("scope", "read")  # Default to 'read' if not specified
    
    if not client_id or not redirect_uri:
        raise ValueError("Missing required environment variables.")

    return client_id, redirect_uri, scope


# next Generate the authorization URL
def generate_auth_url(client_id, redirect_uri, scope):
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
def redirect_user_to_strava(auth_url):
    print("Opening browser for user authorization...")
    webbrowser.open(auth_url)  # Open the authorization URL in the default web browser

# Step 3: Handle the redirect from Strava (capture the authorization code)
def get_auth_code_from_redirect(url):
    
    #let's make sure they put in a valid URL
    if not url.startswith("http"):
        print("Invalid URL. Please ensure you paste the full redirected URL.")
        return None

    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    return query_params.get("code", [None])[0]


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
    #First build your parameters from the env file
    client_id, redirected_url, scope =  build_params()

    #Now build the URL
    auth_url = generate_auth_url(client_id, redirected_url, scope)

    #Now redirect the user to strea
    redirect_user_to_strava(auth_url)
    
    # Get the redirected URL from the user
    redirected_url = input("Paste the redirected URL here: ")
    
    #Get the auth code from the URL response
    auth_code = get_auth_code_from_redirect(redirected_url)
    
    if auth_code:
        print(f"Authorization code: {auth_code}")
        update_env_file("auth_code", auth_code)
    else:
        print("Failed to retrieve authorization code.")