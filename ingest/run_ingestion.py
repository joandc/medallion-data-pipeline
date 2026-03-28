### Import the needed libraries
import json
from datetime import datetime
from pathlib import Path
import requests

# Define API URLs
WEATHER_URL = "https://archive-api.open-meteo.com/v1/archive"
AIR_QUALITY_URL = "https://air-quality-api.open-meteo.com/v1/air-quality"

# Define two cities (for Gold dataset comparison in Part2 Project)
CITIES = [
    {"name": "Toronto", "slug": "toronto", "latitude": 43.65, "longitude": -79.38},
    {"name": "Vancouver", "slug": "vancouver", "latitude": 49.28, "longitude": -123.12},
]

# Set date range
START_DATE = "2024-01-01"
END_DATE = "2025-12-31"

# Define Bronze output folders
WEATHER_DIR = Path("data/bronze/open_meteo_weather")
AIR_QUALITY_DIR = Path("data/bronze/open_meteo_air_quality")

WEATHER_DIR.mkdir(parents=True, exist_ok=True)
AIR_QUALITY_DIR.mkdir(parents=True, exist_ok=True)


# Create a timestamp for filenames using one timestamp for each run
timestamp = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")

# Call the weather API
for city in CITIES:
    weather_params = {
        "latitude": city["latitude"],
        "longitude": city["longitude"],
        "start_date": START_DATE,
        "end_date": END_DATE,
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
        "timezone": "auto",
    }

    weather_response = requests.get(WEATHER_URL, params=weather_params, timeout=30)
    weather_response.raise_for_status()
    weather_data = weather_response.json()

# Save the raw weather JSON (exactly as returned)
for city in CITIES:
    weather_file = WEATHER_DIR / f"{city['slug']}_weather_{timestamp}.json"

    with open(weather_file, "w", encoding="utf-8") as f:
        json.dump(weather_data, f, indent=2)

    print(f"Saved weather Bronze snapshot for {city['name']}")

# Call the air-quality API
for city in CITIES:
    air_quality_params = {
        "latitude": city["latitude"],
        "longitude": city["longitude"],
        "start_date": START_DATE,
        "end_date": END_DATE,
        "hourly": "pm2_5,pm10,us_aqi",
        "timezone": "auto",
    }

    air_quality_response = requests.get(
        AIR_QUALITY_URL, params=air_quality_params, timeout=30
    )
    air_quality_response.raise_for_status()
    air_quality_data = air_quality_response.json()

# Save the raw air-quality JSON without changing the structure
for city in CITIES:
    air_quality_file = AIR_QUALITY_DIR / f"{city['slug']}_air_quality_{timestamp}.json"
    with open(air_quality_file, "w", encoding="utf-8") as f:
        json.dump(air_quality_data, f, indent=2)

    print(f"Saved air-quality Bronze snapshot for {city['name']}")

# Print progress messages
print(f"Saved weather Bronze snapshot for {city['name']}")
print(f"Saved air-quality Bronze snapshot for {city['name']}")
