# core/controller.py
import threading
import time

class Controller:
    def __init__(self):
        # Maintain a list of registered agents.
        self.agents = []

    def register_agent(self, agent):
        """Register an agent with the controller."""
        self.agents.append(agent)

    def broadcast(self, message):
        """Broadcast a message to all agents."""
        for agent in self.agents:
            # Call the agent's receive_message method.
            agent.receive_message(message)

    def run(self):
        """Start all agents concurrently."""
        threads = []
        for agent in self.agents:
            t = threading.Thread(target=agent.run)
            t.start()
            threads.append(t)
        try:
            # Keep the main thread alive until all agents finish (or until interrupted).
            while any(t.is_alive() for t in threads):
                time.sleep(1)
        except KeyboardInterrupt:
            print("Shutting down agents...")
        finally:
            for agent in self.agents:
                agent.stop()
            for t in threads:
                t.join()
