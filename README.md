# Real-Time Data Processing System for Weather Monitoring with Rollups and Aggregates

Overview
This project implements a real-time weather monitoring system that retrieves data from the OpenWeatherMap API for several cities in India. It processes and stores this data in a MySQL database and provides visualizations of the weather data over time. The system also includes alerting functionalities based on user-defined thresholds for temperature and weather conditions.

#Table of Contents
#Features
#Architecture
#Technologies Used
#Setup Instructions
#Dependencies
#How to Run


## Features
  Fetches weather data for specified cities at configurable intervals.
  Stores weather data and daily summaries in a MySQL database.
  Visualizes weather data trends through line charts.
  Sends alerts when temperature thresholds are exceeded.

## Architecture
  The system is composed of the following components:

  Data Fetcher: Continuously fetches weather data from the OpenWeatherMap API.
  Database: MySQL database to store raw weather data and daily summaries.
  Data Processor: Processes the fetched data to generate daily summaries.
  Visualizer: Generates visual representations of the weather data.
  Alert System: Monitors the weather data for defined thresholds and triggers alerts.

## Technologies Used
  Python 3.x
  MySQL (for data storage)
  Matplotlib (for data visualization)
  Requests (for API calls)

## Setup Instructions

1. Clone the Repository:
   Copy code
        git clone https://github.com/your_username/weather-monitoring.git
        cd weather-monitoring
   
2. Install Dependencies: Create a virtual environment and activate it:
   Copy code
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   
   Install required packages:
   Copy code
   pip install -r requirements.txt
   
3. Set Up MySQL Database:
   Create a MySQL database named weather_monitoring.
   Run the SQL scripts included in the repository to set up the necessary tables.

   
4.Configure Environment Variables: Set up your OpenWeatherMap API key and database credentials in your environment variables or directly in the source code.

## Dependencies:

1. MySQL Server: Make sure to have MySQL running locally or use Docker

   docker run --name mysql -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=weather_monitoring -p 3306:3306 -d mysql:latest

2. Python Libraries: Ensure the following libraries are included in requirements.txt:

   mysql-connector-python
   matplotlib
   requests
   pandas

## How to Run

1. Start the MySQL server (if not already running).
  
2. Run the weather data fetcher:
   
   Code: python weather_data_fetcher.py
   
   Code: python weather_data_processor.py

4. To generate visualizations:
   Code: python weather_data_visualization.py

## Test Cases

The project includes test cases to ensure functionality:

1. System Setup: Tests if the system connects to the OpenWeatherMap API successfully.
2. Data Retrieval: Simulates API calls and verifies correct data retrieval.
3. Temperature Conversion: Validates conversion from Kelvin to Celsius.
4. Daily Weather Summary: Simulates weather updates and checks summary calculations.
5. Alerting Thresholds: Ensures alerts are triggered correctly based on temperature thresholds.







