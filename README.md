# Strava API Data Pipeline Project

This project provides tools for retrieving data from the Strava API and processing it for analysis. The code is designed to facilitate the extraction, transformation, and loading (ETL) of Strava activity data into a structured format, enabling further analysis and visualization.

---

![My visualized Strava data](https://github.com/user-attachments/assets/fc452f7c-74bb-46f8-882c-c419da843448)

## Table of Contents

1. [Project Overview](#project-overview)  
2. [Features](#features)  
3. [Installation](#installation)  
4. [Power BI Installation](#power-bi-installation)  
5. [Configuration](#configuration)  
6. [Usage](#usage)  

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

   Install the required Python packages by running:

   ```bash
   pip install -r requirements.txt
   ```

---

## Power BI Installation

To visualize your Strava data, you'll need **Power BI Desktop** installed on your system.

1. **Download Power BI Desktop**:
   - Go to the [Power BI Download Page](https://powerbi.microsoft.com/en-us/downloads/).
   - Click on "Download free" to get the latest version of Power BI Desktop.

2. **Install Power BI Desktop**:
   - Run the downloaded installer and follow the installation prompts.
   - After installation, launch **Power BI Desktop**.

3. **Verify Installation**:
   - Open **Power BI Desktop** and confirm it loads correctly.

---

## Configuration

1. **Set up Strava API credentials**:

   - Go to the [Strava API Settings](https://www.strava.com/settings/api) and create an application.  
   - Obtain the `Client ID` and `Client Secret`.

2. **Update the configuration file**:

   Open the `.env` file in the root directory and update the following values:

   ```env
   CLIENT_ID=your_client_id
   CLIENT_SECRET=your_client_secret
   ```

---

## Usage

1. **Run the data extraction script**:

   ```bash
   python _Main.py
   ```

   - If you have not previously authorized the project, you will be routed to an authorization prompt on Strava's website.  
   - Grant authorization and copy & paste the URL into the input prompt in the Python terminal.
   - The application will parse the authorization code from the pasted URL and update your `.env` file.

   Execute the `_Main.py` script once more, and your Strava activities will be extracted and saved as a local CSV file.

2. **Review the output**:

   Check the `strava_activities.csv` file containing the processed activity data.

3. **Open the Power BI Report**:

   - Navigate to the `Report` directory and open the file **`Strava Report.pbip`** in Power BI Desktop.

4. **Update the Connection String**:

   - In Power BI, modify the connection string of the `strava_activities` dataset so it matches the location where your `strava_activities.csv` file is saved.
   - After updating the connection, refresh the report to visualize your Strava data.

---

### Enjoy Visualizing Your Data!

