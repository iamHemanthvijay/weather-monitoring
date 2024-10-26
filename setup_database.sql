-- Create database
CREATE DATABASE IF NOT EXISTS weather_monitoring;

-- Use the database
USE weather_monitoring;

-- Create table for storing raw weather data
CREATE TABLE IF NOT EXISTS weather_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    city VARCHAR(50) NOT NULL,
    main VARCHAR(50) NOT NULL,
    temp FLOAT NOT NULL,
    feels_like FLOAT NOT NULL,
    dt DATETIME NOT NULL,
    UNIQUE KEY (city, dt)
);

-- Create table for storing daily weather summaries
CREATE TABLE IF NOT EXISTS daily_weather_summary (
    id INT AUTO_INCREMENT PRIMARY KEY,
    city VARCHAR(50) NOT NULL,
    summary_date DATE NOT NULL,
    avg_temp FLOAT NOT NULL,
    max_temp FLOAT NOT NULL,
    min_temp FLOAT NOT NULL,
    dominant_condition VARCHAR(50) NOT NULL,
    UNIQUE KEY (city, summary_date)
);

-- Optionally, insert initial data for testing
INSERT INTO weather_data (city, main, temp, feels_like, dt)
VALUES 
    ('Delhi', 'Clear', 30.5, 31.2, '2024-10-24 10:00:00'),
    ('Delhi', 'Haze', 31.0, 31.5, '2024-10-25 10:00:00'),
    ('Delhi', 'Clouds', 29.0, 29.5, '2024-10-26 10:00:00');

-- Insert initial daily summaries if needed
INSERT INTO daily_weather_summary (city, summary_date, avg_temp, max_temp, min_temp, dominant_condition)
VALUES 
    ('Delhi', '2024-10-24', 30.5, 31.5, 29.5, 'Clear'),
    ('Delhi', '2024-10-25', 30.0, 31.0, 29.0, 'Haze'),
    ('Delhi', '2024-10-26', 29.0, 30.0, 29.0, 'Clouds');
