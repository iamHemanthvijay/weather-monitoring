import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="Adhiveer",
        password="Harsha@luci@321",
        database="weather_monitoring"
    )

def fetch_daily_summaries(city):
    db_connection = connect_to_database()
    cursor = db_connection.cursor()
    
    sql = "SELECT summary_date, avg_temp, max_temp, min_temp FROM daily_weather_summary WHERE city = %s"
    cursor.execute(sql, (city,))
    
    data = cursor.fetchall()
    cursor.close()
    db_connection.close()
    
    return data

def plot_daily_summary(cities):
    plt.figure(figsize=(12, 6))

    for city in cities:
        data = fetch_daily_summaries(city)

        if not data:
            print(f"No data found for {city}.")
            continue

        df = pd.DataFrame(data, columns=['summary_date', 'avg_temp', 'max_temp', 'min_temp'])
        df['summary_date'] = pd.to_datetime(df['summary_date'])
        df.set_index('summary_date', inplace=True)

        # Plot each city's data
        plt.plot(df.index, df['avg_temp'], label=f'{city} Avg Temp', marker='o')
        plt.plot(df.index, df['max_temp'], label=f'{city} Max Temp', linestyle='--', marker='o')
        plt.plot(df.index, df['min_temp'], label=f'{city} Min Temp', linestyle=':', marker='o')

    plt.title('Daily Weather Summary for All Cities')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.legend()
    plt.grid()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# List of cities to visualize
cities = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]

# Call the plot function for all cities
plot_daily_summary(cities)
