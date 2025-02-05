# agents/analyzer.py
from agents.base_agent import BaseAgent

class Analyzer(BaseAgent):
    def do_work(self):
        # Check if there are any messages (weather data) to analyze.
        if not self.message_queue.empty():
            while not self.message_queue.empty():
                msg = self.message_queue.get()
                # Check if the message contains weather data.
                if "weather_data" in msg:
                    weather = msg["weather_data"]
                    analysis = f"Analyzing weather for {weather.get('city')}: " \
                               f"{weather.get('temperature')}°C, " \
                               f"{weather.get('weather')}, " \
                               f"Humidity: {weather.get('humidity')}%"
                    print(f"[{self.name}] {analysis}")
                else:
                    print(f"[{self.name}] Received non-weather message: {msg}")
        else:
            print(f"[{self.name}] No new data to analyze.")
