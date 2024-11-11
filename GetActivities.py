import requests
import time  # Optional for rate limits
import pandas as pd
# Replace with your access token
access_token = "9938f3180a3ee5f538e4b1a76456023e18631c82"



# Define the endpoint URL for fetching activities
activities_url = "https://www.strava.com/api/v3/athlete/activities"

# Headers with the access token for authentication
headers = {
    "Authorization": f"Bearer {access_token}"
}

# Initialize a list to store all activities and set the first page
all_activities = []
page = 1

# Loop to keep fetching activities until no more are returned
while True:
    # Request parameters for pagination
    params = {
        "page": page,
        "per_page": 30  # The maximum allowed per request
    }

    # Make the API request to fetch activities for the current page
    response = requests.get(activities_url, headers=headers, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        activities = response.json()

        # Break if no more activities are returned
        if not activities:
            break

        # Add the current page of activities to the full list
        all_activities.extend(activities)

        # Print progress (optional)
        print(f"Fetched page {page}, retrieved {len(activities)} activities")

        # Increment to fetch the next page
        page += 1

        # Optional: Small delay to avoid rate limiting
        time.sleep(1)
    else:
        print("Error fetching activities:", response.json())
        break

# Display the total number of activities fetched
print(f"Total activities retrieved: {len(all_activities)}")


# Convert the list of activities to a pandas DataFrame
activities_df = pd.DataFrame(all_activities)

# Save the DataFrame to a CSV file
activities_df.to_csv("strava_activities.csv", index=False)

print("Activities saved to strava_activities.csv")