# Strava API Data Pipeline Project

This project provides tools for retrieving data from the Strava API and processing it for analysis. The code is designed to facilitate the extraction, transformation, and loading (ETL) of Strava activity data into a structured format, enabling further analysis and visualization.

---![My visualized Strava data](https://github.com/user-attachments/assets/fc452f7c-74bb-46f8-882c-c419da843448)



## Table of Contents

1. [Project Overview](#project-overview)  
2. [Features](#features)  
3. [Installation](#installation)  
4. [Configuration](#configuration)  
5. [Usage](#usage)  
   

---

## Project Overview

This project leverages Strava's API to retrieve activity data, process it, and export it to formats suitable for analysis (e.g., CSV). It supports fetching details about individual runs, rides, or other activities and transforming the raw data for easy exploration and reporting.

## Features

- **Authentication**: Handles OAuth2 authentication with Strava's API.
- **Data Retrieval**: Fetches data from Strava, such as activity details (distance, pace, time, etc.).
- **Data Processing**: Cleans and transforms the data into a structured format.
- **Export to CSV**: Exports processed data to CSV for further use in analysis tools like Power BI or Excel.
- **Data Visualization**: Visualizes your Strava data in a Power BI report, enabling you to analyze your running activity.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/RDNelson00/Strava-Stream-.git

   ```


2. **Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. **Set up Strava API credentials**:

   - Go to the [Strava API Settings](https://www.strava.com/settings/api) and create an application.
   - Obtain the `Client ID` and `Client Secret`.

2. **Update the configuration file**:

   Open the `.env` file in the root directory update the following values:

   ```env
   CLIENT_ID=your_client_id
   CLIENT_SECRET=your_client_secret
   ```

## Usage

1. **Run the data extraction script**:

   ```bash
   python _Main.py
   ```
   If you have not previously authorized the project, you will be routed to an authorization prompt on Strava's website. Grant authorization and copy & paste the URL into the input prompt in the Python terminal.
   The application will parse the authorization code from the pasted URL and update your env file.

   Execute the _Main.py script once more, and your Strava activities will be extracted and saved as a local CSV file.

1. **Review the output**:

   Check the `strava_activities.csv` file containing the processed activity data.

2. **Open the file 'Strava Report.PBIP' in the 'Report' folder of the project directory.**

   You will need to modify the connection string of the 'strava_activities' file so it matches the save location of your locally stored strava_activities.csv file.
   After the connection is updated, the report will refresh with your Strava data. 



