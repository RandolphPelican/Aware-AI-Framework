class TemporalDemodulator:
    def __init__(self):
        self.state = None

    def update(self, frame):
        self.state = frame

    def get_state(self):
        return self.state
