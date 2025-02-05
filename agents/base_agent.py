# agents/base_agent.py
import threading
import queue

class BaseAgent:
    def __init__(self, name, controller):
        self.name = name
        self.controller = controller
        self.running = False
        # Use a thread-safe queue for incoming messages.
        self.message_queue = queue.Queue()

    def receive_message(self, message):
        """Receive and enqueue a message."""
        self.message_queue.put(message)

    def process_messages(self):
        """Process all messages in the queue."""
        while not self.message_queue.empty():
            msg = self.message_queue.get()
            print(f"[{self.name}] Processed message: {msg}")

    def run(self):
        """Main loop for the agent. Override this method in subclasses."""
        self.running = True
        while self.running:
            self.process_messages()
            self.do_work()
            # Sleep briefly to allow other threads to run.
            threading.Event().wait(1)

    def do_work(self):
        """Perform agent-specific work (to be implemented in subclasses)."""
        raise NotImplementedError

    def stop(self):
        """Stop the agent's main loop."""
        self.running = False
