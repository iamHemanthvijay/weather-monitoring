import time
from datetime import datetime, timezone
import requests
import mysql.connector

# Function to connect to MySQL database
def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="Adhiveer",    # Your MySQL username
        password="Harsha@luci@321", # Your MySQL password
        database="weather_monitoring"
    )

def kelvin_to_celsius(temp_kelvin):
    return temp_kelvin - 273.15  # Convert Kelvin to Celsius

def get_weather_data(city_name, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather_info = {
            "city": city_name,
            "main": data['weather'][0]['main'],
            "temp": data['main']['temp'],  # Already in Celsius
            "feels_like": data['main']['feels_like'],  # Already in Celsius
            "dt": datetime.fromtimestamp(data['dt'], timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
        }
        return weather_info
    else:
        print(f"Error: {response.status_code} for {city_name}")
        return None

def insert_weather_data(cursor, weather_data):
    sql = "INSERT INTO weather_data (city, main, temp, feels_like, dt) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql, (weather_data['city'], weather_data['main'], weather_data['temp'], weather_data['feels_like'], weather_data['dt']))
    print(f"Inserted data: {weather_data}")  # Debug statement

def continuously_fetch_weather(cities, api_key, interval=300):
    db_connection = connect_to_database()
    cursor = db_connection.cursor()

    while True:
        for city in cities:
            weather_data = get_weather_data(city, api_key)
            if weather_data:
                insert_weather_data(cursor, weather_data)  # Insert into MySQL
                db_connection.commit()  # Commit the transaction
                print(f"Weather data inserted for {city}: {weather_data}")  # Debug statement

                # Process daily summaries after inserting data
                process_daily_summaries()  # Ensure this is called here
            else:
                print("Failed to retrieve data.")

        time.sleep(interval)  # Wait for the next fetch cycle
        
from datetime import datetime, timedelta

def insert_daily_summary(cursor, city, summary_date, avg_temp, max_temp, min_temp, dominant_condition):
    sql = """
    INSERT INTO daily_weather_summary (city, summary_date, avg_temp, max_temp, min_temp, dominant_condition)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(sql, (city, summary_date, avg_temp, max_temp, min_temp, dominant_condition))
    print(f"Inserted daily summary for {city} on {summary_date}: Avg: {avg_temp}, Max: {max_temp}, Min: {min_temp}, Condition: {dominant_condition}")  # Debug statement

def calculate_daily_summary(db_connection, cursor, city, date):
    sql = """
    SELECT AVG(temp) AS avg_temp, MAX(temp) AS max_temp, MIN(temp) AS min_temp, 
           (SELECT main FROM weather_data WHERE city = %s AND DATE(dt) = %s GROUP BY main ORDER BY COUNT(*) DESC LIMIT 1) AS dominant_condition
    FROM weather_data
    WHERE city = %s AND DATE(dt) = %s
    """
    
    cursor.execute(sql, (city, date, city, date))
    result = cursor.fetchone()

    if result and result[0] is not None:  # Ensure we have valid data
        avg_temp = result[0]
        max_temp = result[1]
        min_temp = result[2]
        dominant_condition = result[3] or "Unknown"
        insert_daily_summary(cursor, city, date, avg_temp, max_temp, min_temp, dominant_condition)
    else:
        print(f"No valid data to summarize for {city} on {date}.")  # Debug statement

def process_daily_summaries():
    db_connection = connect_to_database()
    cursor = db_connection.cursor()
    today = datetime.now().date()

    for city in ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]:  # Add your cities
        # Check if a summary already exists for today
        cursor.execute("SELECT COUNT(*) FROM daily_weather_summary WHERE city = %s AND summary_date = %s", (city, today))
        if cursor.fetchone()[0] == 0:
            calculate_daily_summary(db_connection, cursor, city, today)
        else:
            print(f"Daily summary already exists for {city} on {today}.")  # Debug statement

    db_connection.commit()
    cursor.close()
    db_connection.close()

# Define thresholds
temperature_threshold = 35.0  # Example threshold
alert_count = 0

def check_alert_conditions(weather_data):
    global alert_count

    if weather_data['temp'] > temperature_threshold:
        alert_count += 1
        if alert_count >= 2:  # Two consecutive updates over the threshold
            print(f"Alert: {weather_data['city']} temperature exceeded {temperature_threshold}°C!")
            alert_count = 0  # Reset after alert
    else:
        alert_count = 0  # Reset if below threshold

# Main execution
if __name__ == "__main__":
    api_key = "0cfe2d0166ba8ec4725356a2d88b0737"  # Replace with your actual API key
    cities = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]

    continuously_fetch_weather(cities, api_key)
