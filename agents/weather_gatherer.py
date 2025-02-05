# agents/weather_gatherer.py
import requests
from agents.base_agent import BaseAgent

class WeatherDataGatherer(BaseAgent):
    def __init__(self, name, controller, api_key, city):
        super().__init__(name, controller)
        self.api_key = api_key
        self.city = city
        # Base URL for current weather data (units=metric for Celsius)
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    def do_work(self):
        # Build request parameters.
        params = {
            "q": self.city,
            "appid": self.api_key,
            "units": "metric"
        }
        try:
            response = requests.get(self.base_url, params=params, timeout=5)
            response.raise_for_status()
            data = response.json()
            weather_info = {
                "city": self.city,
                "temperature": data.get("main", {}).get("temp"),
                "weather": data.get("weather", [{}])[0].get("description"),
                "humidity": data.get("main", {}).get("humidity")
            }
            print(f"[{self.name}] Fetched weather data: {weather_info}")
            # Broadcast the weather data to other agents.
            self.controller.broadcast({"from": self.name, "weather_data": weather_info})
        except requests.RequestException as e:
            print(f"[{self.name}] Error fetching data: {e}")
