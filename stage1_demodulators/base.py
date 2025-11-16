class BaseDemodulator:
    def __init__(self):
        self.state = None

    def update(self, frame):
        self.state = frame

    def get_state(self):
        return self.state

    # Add this method
    def process_frame(self, frame):
        """
        Simulate processing a sensory frame and returning processed data.
        """
        self.update(frame)
        return {"processed_frame": self.get_state()}
