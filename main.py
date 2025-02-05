# main.py
from core.controller import Controller
from agents.weather_gatherer import WeatherDataGatherer
from agents.analyzer import Analyzer
from agents.responder import Responder

def main():
    # Replace with your actual OpenWeather API key and desired city.
    OPENWEATHER_API_KEY = "your_api_key"
    CITY = "London"  # Example city; change as needed.

    # Create the central controller.
    controller = Controller()

    # Create agents.
    weather_agent = WeatherDataGatherer("WeatherGatherer", controller, OPENWEATHER_API_KEY, CITY)
    analyzer_agent = Analyzer("Analyzer", controller)
    responder_agent = Responder("Responder", controller)

    # Register agents with the controller.
    controller.register_agent(weather_agent)
    controller.register_agent(analyzer_agent)
    controller.register_agent(responder_agent)

    print("Starting agentic AI system (using OpenWeather API). Press Ctrl+C to exit.")
    controller.run()

if __name__ == "__main__":
    main()
