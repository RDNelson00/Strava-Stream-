import requests

# Replace these with your actual credentials and auth code
client_id = "135951"
client_secret = "46965ce118254df90f540bdc8abbf88de8130cf3"
auth_code = "a38822d94f5acabce093e09ea492d82e1adbe1e1"

# Request URL for exchanging the authorization code
token_url = "https://www.strava.com/oauth/token"

# Define the parameters for the token request
payload = {
    'client_id': client_id,
    'client_secret': client_secret,
    'code': auth_code,
    'grant_type': 'authorization_code'
}

# Send the POST request
response = requests.post(token_url, data=payload)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    access_token = data['access_token']
    refresh_token = data['refresh_token']
    print("Access Token:", access_token)
    print("Refresh Token:", refresh_token)
else:
    print("Failed to obtain token:", response.json())
