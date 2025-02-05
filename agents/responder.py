# agents/responder.py
from agents.base_agent import BaseAgent

class Responder(BaseAgent):
    def do_work(self):
        # Check if there are any messages.
        if not self.message_queue.empty():
            while not self.message_queue.empty():
                msg = self.message_queue.get()
                if "weather_data" in msg:
                    weather = msg["weather_data"]
                    response = f"Responder: The current weather in {weather.get('city')} is " \
                               f"{weather.get('weather')} with a temperature of {weather.get('temperature')}°C."
                    print(f"[{self.name}] {response}")
                else:
                    print(f"[{self.name}] Received message: {msg}")
        else:
            print(f"[{self.name}] Waiting for weather updates...")
