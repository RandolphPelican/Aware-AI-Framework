# ai_core/demodulator.py

"""
General Demodulator Module
Provides a base class for all demodulators in the Aware-AI framework.
"""

class BaseDemodulator:
    def __init__(self, buffer_size=10):
        self.buffer_size = buffer_size
        self.frame_buffer = []

    def update(self, frame):
        """
        Add a new frame to the buffer and maintain max size.
        """
        self.frame_buffer.append(frame)
        if len(self.frame_buffer) > self.buffer_size:
            self.frame_buffer.pop(0)

    def get_state(self):
        """
        Return the aggregated state of recent frames.
        """
        if not self.frame_buffer:
            return None
        # Example: return the latest frame
        return self.frame_buffer[-1]

    def reset(self):
        """
        Clear the frame buffer.
        """
        self.frame_buffer = []
