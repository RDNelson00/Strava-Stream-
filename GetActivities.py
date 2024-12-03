import requests
from datetime import datetime
import pandas as pd
import json
from dotenv import load_dotenv
import os

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

def get_last_fetched_datetime():
    """Retrieve the timestamp of the last fetched activity."""
    try:
        with open(last_fetched_file, 'r') as f:
            data = json.load(f)
            return data.get('last_fetched_epoch')
    except:
        # If the file doesn't exist, return None (meaning start from the beginning)
        return None

def save_last_fetched_datetime(timestamp): 
    """Save the timestamp of the last fetched activity as date/time and epoch."""
    
    # Convert timestamp string to datetime object, handling the 'T' and 'Z' format
    timestamp_dt = datetime.strptime(timestamp.replace("Z", ""), "%Y-%m-%dT%H:%M:%S")
    
    # Convert datetime to epoch time
    epoch_time = int(timestamp_dt.timestamp())
    
    # Create a dictionary with both datetime and epoch
    data = {
        'last_fetched_datetime': timestamp,
        'last_fetched_epoch': epoch_time
    }

    # Save both the datetime and epoch to the file
    with open(last_fetched_file, 'w') as f:
        json.dump(data, f)

    print(f"Saved last fetched datetime and epoch: {data}")


def get_most_recent_timestamp(activities):
    """Get the most recent activity's timestamp."""
    # Sort activities by start_date to ensure we get the most recent one
    activities_sorted = sorted(activities, key=lambda x: x['start_date'], reverse=True)
    
    # Get the most recent activity (first in the sorted list)
    return activities_sorted[0]['start_date'] if activities_sorted else None

def fetch_activities(access_token, activities_url, per_page=200, after=None):
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
            params["page"] = page
        elif response.status_code == 429:  # Rate limit error
            print("Rate limit exceeded. Saving activities.")
            break
        else:
            print("Error fetching activities:", response.json())
            break

    print(f"Total activities retrieved: {len(all_activities)}")
    return all_activities


def save_activities_to_csv(activities, filename="strava_activities.csv"):
    """Save activities to a CSV file."""
    #first see how many records exist in the file
    try:
        df = pd.read_csv(filename)
        row_count = len(df)
        print("Number of records:", row_count)    
    except:
        print ("Activities file not found")



    # Check if the file exists and whether it is empty or not
    if not os.path.isfile(filename):
        # If the file doesn't exist, create it and write the activities with headers
        print ("Activities file does not exist, writing new file")
        activities_df = pd.DataFrame(activities)

        
        activities_df.to_csv(filename, index=False, mode='w', header=True)
        print(f"Created new file and saved activities to {filename}")
    
    else:
        # If the file exists and is not empty, append without headers
        print("Activities file exists with data, appending w/o headers")
        os.chmod(filename, 0o644)  # Make the file writable
        activities_df = pd.DataFrame(activities)
       
       # Ensure the new data matches the column structure of the existing file
        existing_df = pd.read_csv(filename, nrows=0)  # Load just the headers
        activities_df = activities_df.reindex(columns=existing_df.columns, fill_value=None)

        # Append the data
        activities_df.to_csv(filename, index=False, mode='a', header=False)
        print(f"Appended activities to {filename}")

        # After saving, make the file read-only
        os.chmod(filename, 0o444)  # Read-only permission for the file (Owner, Group, Others)









def main():
    # Get the access token
    access_token = get_access_token()

    if access_token:
        print("Access token retrieved:", access_token)

        # Get the timestamp of the last fetched activity (if any)
        last_fetched_datetime = get_last_fetched_datetime()

        # Fetch activities incrementally
        activities = fetch_activities(access_token, activities_url, after=last_fetched_datetime)
        

        if activities:
            # Get the most recent timestamp
            most_recent_timestamp = get_most_recent_timestamp(activities)
            if most_recent_timestamp:
                print(f"Most recent timestamp: {most_recent_timestamp}")
                # Save the most recent timestamp
                save_last_fetched_datetime(most_recent_timestamp)

            # Save activities to CSV
            save_activities_to_csv(activities)
        else:
            print("No activities fetched.")
    else:
        print("No access token found or file error.")

if __name__ == "__main__":
    main()
