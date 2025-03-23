import httpx
from dotenv import load_dotenv
import os

# Загружаем переменные из .env
load_dotenv()
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
if not WEATHER_API_KEY:
    raise ValueError("Missing WEATHER_API_KEY in .env file")

async def get_forecast(city: str) -> str:
    """Fetch current weather forecast for a city anywhere in the world."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, timeout=10.0)
            response.raise_for_status()
            data = response.json()
            return f"""
City: {data['name']}, {data['sys']['country']}
Temperature: {data['main']['temp']}°C
Weather: {data['weather'][0]['description']}
Wind: {data['wind']['speed']} m/s, direction {data['wind']['deg']}°
Humidity: {data['main']['humidity']}%
"""
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 404:
                return f"City {city} not found."
            return "Unable to fetch weather data."
        except Exception:
            return "Unable to fetch weather data."
