# Strava API Data Pipeline Project

This project provides tools for retrieving data from the Strava API and processing it for analysis. The code is designed to facilitate the extraction, transformation, and loading (ETL) of Strava activity data into a structured format, enabling further analysis and visualization.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Configuration](#configuration)
5. [Usage](#usage)
6. [Project Structure](#project-structure)
7. [Dependencies](#dependencies)
   

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
   git clone [https://github.com/your-username/strava-api-pipeline](https://github.com/RDNelson00/Strava-Stream-).git
   cd Strava-Stream-
   ```


2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. **Set up Strava API credentials**:

   - Go to the [Strava API Settings](https://www.strava.com/settings/api) and create an application.
   - Obtain the `Client ID`, `Client Secret`, and `Refresh Token`.

2. **Update the configuration file**:

   Create a `.env` file in the root directory with the following content:

   ```env
   CLIENT_ID=your_client_id
   CLIENT_SECRET=your_client_secret
   REFRESH_TOKEN=your_refresh_token
   ```

## Usage

1. **Run the data extraction script**:

   ```bash
   python main.py
   ```

   This will authenticate with the Strava API, fetch activity data, and export it to a CSV file.

2. **Review the output**:

   Check the `strava_activities.csv` file containing the processed activity data.


## Dependencies

- **Python 3.8+**
- **Libraries**:
  - `requests`
  - `pandas`
  - `python-dotenv`

Install dependencies with:

```bash
pip install -r requirements.txt
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

