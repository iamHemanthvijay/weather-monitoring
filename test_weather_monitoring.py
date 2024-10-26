import requests

def test_system_setup(api_key):
    try:
        response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q=Delhi&appid={api_key}")
        assert response.status_code == 200
        print("System setup test passed: Successfully connected to the API.")
    except Exception as e:
        print(f"System setup test failed: {e}")

# Example usage
test_system_setup("0cfe2d0166ba8ec4725356a2d88b0737")

def get_weather_data(city_name, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()  # Return parsed JSON data
    else:
        print(f"Error: {response.status_code} for {city_name}")
        return None

def test_data_retrieval(api_key, cities):
    for city in cities:
        weather_data = get_weather_data(city, api_key)
        assert weather_data is not None, f"Data retrieval failed for {city}."
    print("Data retrieval test passed.")

# Example usage
#test_data_retrieval("", ["Delhi", "Mumbai", "Chennai"])

def get_weather_data(city_name, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()  # Return parsed JSON data
    else:
        print(f"Error: {response.status_code} for {city_name}")
        return None

def test_data_retrieval(api_key, cities):
    for city in cities:
        weather_data = get_weather_data(city, api_key)
        assert weather_data is not None, f"Data retrieval failed for {city}."
    print("Data retrieval test passed.")

# Example usage
test_data_retrieval("0cfe2d0166ba8ec4725356a2d88b0737", ["Delhi", "Mumbai", "Chennai","Bangalore", "Kolkata", "Hyderabad"])

def kelvin_to_celsius(temp_kelvin):
    return temp_kelvin - 273.15  # Convert Kelvin to Celsius

def test_temperature_conversion():
    kelvin_temp = 300  # Example temperature in Kelvin
    expected_celsius = kelvin_to_celsius(kelvin_temp)
    assert abs(expected_celsius - 26.85) < 0.01, "Temperature conversion test failed."
    print("Temperature conversion test passed.")

# Example usage
test_temperature_conversion()



import mysql.connector
from datetime import datetime, timedelta
from weather_data_fetcher import process_daily_summaries  # Import the function from the appropriate module

# Function to connect to MySQL database
def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="Adhiveer",
        password="Harsha@luci@321",
        database="weather_monitoring"
    )

def insert_weather_data(cursor, weather_data):
    sql = "INSERT INTO weather_data (city, main, temp, feels_like, dt) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql, (weather_data['city'], weather_data['main'], weather_data['temp'], weather_data['feels_like'], weather_data['dt']))

def test_daily_weather_summary():
    # Simulate weather data for the last three days
    simulated_data = [
        {'city': 'Delhi', 'temp': 30, 'feels_like': 32, 'dt': (datetime.now() - timedelta(days=2)).strftime('%Y-%m-%d %H:%M:%S'), 'main': 'Clear'},
        {'city': 'Delhi', 'temp': 31, 'feels_like': 33, 'dt': (datetime.now() - timedelta(days=2, hours=1)).strftime('%Y-%m-%d %H:%M:%S'), 'main': 'Clear'},
        {'city': 'Delhi', 'temp': 29, 'feels_like': 31, 'dt': (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S'), 'main': 'Cloudy'},
        {'city': 'Delhi', 'temp': 32, 'feels_like': 34, 'dt': (datetime.now() - timedelta(days=1, hours=1)).strftime('%Y-%m-%d %H:%M:%S'), 'main': 'Cloudy'},
        {'city': 'Delhi', 'temp': 31, 'feels_like': 33, 'dt': (datetime.now()).strftime('%Y-%m-%d %H:%M:%S'), 'main': 'Haze'},
        {'city': 'Delhi', 'temp': 28, 'feels_like': 30, 'dt': (datetime.now() - timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S'), 'main': 'Haze'},
    ]
    
    db_connection = connect_to_database()
    cursor = db_connection.cursor()
    
    # Insert simulated data into the weather_data table
    for data in simulated_data:
        insert_weather_data(cursor, data)
    
    db_connection.commit()
    
    # Call your daily summary processing function
    process_daily_summaries()  # Ensure this function processes the data correctly
    
    # Verify that the summary was calculated
    cursor.execute("SELECT * FROM daily_weather_summary WHERE city = 'Delhi'")
    summary = cursor.fetchall()
    
    assert summary is not None and len(summary) > 0, "Daily summary calculation failed."
    
    # Print out the summary for verification
    for row in summary:
        print(row)
    
    print("Daily weather summary test passed.")

# Run the test case
if __name__ == "__main__":
    test_daily_weather_summary()
    
    
import mysql.connector
from mysql.connector import Error

temperature_threshold = 30.0  # Set a sample threshold

def check_alert_conditions(weather_data):
    global alert_count
    if weather_data['temp'] > temperature_threshold:
        alert_count += 1
        if alert_count >= 2:  # Trigger alert on two consecutive breaches
            print(f"Alert: {weather_data['city']} temperature exceeded {temperature_threshold}°C!")
            alert_count = 0  # Reset after alert
    else:
        alert_count = 0  # Reset if below threshold

def test_alerting_thresholds():
    global alert_count
    alert_count = 0  # Reset alert count before testing

    test_data = [
        {'city': 'Delhi', 'temp': 32},
        {'city': 'Delhi', 'temp': 29},
    ]

    for weather in test_data:
        check_alert_conditions(weather)
    
    # Ensure that the alert was triggered for the first condition
    assert alert_count == 0, "Alerting thresholds test failed: Alert not triggered as expected."
    
    print("Alerting thresholds test passed.")

# Example usage
test_alerting_thresholds()
















