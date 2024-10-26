import mysql.connector

def connect_to_database():
    # Adjust the connection parameters as needed
    return mysql.connector.connect(
        host="localhost",
        user="Adhiveer",
        password="Harsha@luci@321",
        database="weather_monitoring"
    )

# Create a table for daily summaries (run this once to set up the table)
def create_daily_summary_table():
    db_connection = connect_to_database()
    cursor = db_connection.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS daily_weather_summary (
        id INT AUTO_INCREMENT PRIMARY KEY,
        city VARCHAR(50),
        summary_date DATE,
        avg_temp FLOAT,
        max_temp FLOAT,
        min_temp FLOAT,
        dominant_condition VARCHAR(50)
    )
    """)
    
    db_connection.commit()
    cursor.close()
    db_connection.close()

# Call this function once to create the table
create_daily_summary_table()
