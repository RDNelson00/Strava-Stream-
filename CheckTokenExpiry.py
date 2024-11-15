import requests
import time  # Optional for rate limits
import pandas as pd
import json
from dotenv import load_dotenv

token_file = 'strava_tokens.json'
 
def get_token_expiry():
    with open(token_file, 'r') as f:
        tokens = json.load(f)
        return tokens.get('expires_at')  # Extract the refresh token

expiry = get_token_expiry()

if access_token:
    print("Access token retrieved:", access_token)
else:
    print("No access token found or file error.")
