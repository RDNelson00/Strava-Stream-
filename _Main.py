import json
from datetime import datetime, timezone
import RefreshToken
import GetActivities

token_file = 'strava_tokens.json'
 
def get_token_expiry():
    with open(token_file, 'r') as f:
        tokens = json.load(f)
        return tokens.get('issued_at')  # Extract the refresh token

expiry = get_token_expiry()

#convert the unix timestamp to UTC
expiry = datetime.fromtimestamp(expiry, tz=timezone.utc)
print("Access token expires at", expiry, ". Right now it is", datetime.now(timezone.utc))

#check if the token is expired

#if its expired, refresh it
if expiry < datetime.now(timezone.utc):
    exec (RefreshToken)
#if not, get the activities
else:
    exec(GetActivities)