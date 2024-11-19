import requests
import time  # Optional for rate limits
import pandas as pd
import json
from dotenv import load_dotenv

token_file = 'strava_tokens.json'
activities_url = "https://www.strava.com/api/v3/athlete/activities"
last_fetched_file = 'last_fetched.json'  # File to store the timestamp of the last fetched activity

def get_access_token():
    """Retrieve the Strava API access token from a file."""
    try:
        with open(token_file, 'r') as f:
            tokens = json.load(f)
            access_token = tokens.get('access_token')  # Extract the access token
            if access_token:
                return access_token
            else:
                print("Access token not found in the file.")
                return None
    except FileNotFoundError:
        print(f"{token_file} not found. Please ensure the file exists.")
        return None

def get_last_fetched_timestamp():
    """Retrieve the timestamp of the last fetched activity."""
    try:
        with open(last_fetched_file, 'r') as f:
            data = json.load(f)
            return data.get('last_fetched_timestamp')
    except FileNotFoundError:
        # If the file doesn't exist, return None (meaning start from the beginning)
        return None

def save_last_fetched_timestamp(timestamp):
    """Save the timestamp of the last fetched activity."""
    with open(last_fetched_file, 'w') as f:
        json.dump({'last_fetched_timestamp': timestamp}, f)

def fetch_activities(access_token, activities_url, per_page=30, after=None):
    """Fetch activities from the Strava API with pagination and filter by timestamp."""
    all_activities = []
    page = 1
    headers = {"Authorization": f"Bearer {access_token}"}
    params = {"page": page, "per_page": per_page}
    
    if after:
        params["after"] = after  # Only fetch activities after the specified timestamp

    while True:
        response = requests.get(activities_url, headers=headers, params=params)

        if response.status_code == 200:
            activities = response.json()
            if not activities:  # No more activities to fetch
                break
            all_activities.extend(activities)
            print(f"Fetched page {page}, retrieved {len(activities)} activities")
            page += 1

            # Update 'after' to the timestamp of the most recent activity
            most_recent_activity = activities[-1]
            most_recent_timestamp = most_recent_activity['start_date']  # Example timestamp
            save_last_fetched_timestamp(most_recent_timestamp)

        elif response.status_code == 429:  # Rate limit error
            reset_time = response.headers.get('X-RateLimit-Reset')
            if reset_time:
                reset_time = int(reset_time)  # Convert to integer
                wait_time = reset_time - time.time()
                print(f"Rate limit exceeded, waiting for {wait_time} seconds.")
                time.sleep(wait_time)  # Sleep until the rate limit resets
            else:
                print("Rate limit exceeded, but no reset time found. Retrying...")
                time.sleep(60)  # Wait for 1 minute before retrying

        else:
            print("Error fetching activities:", response.json())
            break

    print(f"Total activities retrieved: {len(all_activities)}")
    return all_activities

def save_activities_to_csv(activities, filename="strava_activities.csv"):
    """Save activities to a CSV file."""
    activities_df = pd.DataFrame(activities)
    activities_df.to_csv(filename, index=False)
    print(f"Activities saved to {filename}")

def main():
    # Get the access token
    access_token = get_access_token()

    if access_token:
        print("Access token retrieved:", access_token)

        # Get the timestamp of the last fetched activity (if any)
        last_fetched_timestamp = get_last_fetched_timestamp()
        print(f"Last fetched timestamp: {last_fetched_timestamp}")

        # Fetch activities incrementally
        activities = fetch_activities(access_token, activities_url, after=last_fetched_timestamp)

        # Save activities to CSV
        save_activities_to_csv(activities)
    else:
        print("No access token found or file error.")

if __name__ == "__main__":
    main()
