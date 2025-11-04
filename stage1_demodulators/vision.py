# stage1_demodulators/vision.py

"""
Vision Demodulator Module
Handles spatial pattern recognition and preprocessing of visual inputs.
"""

class VisionDemodulator:
    def __init__(self, resolution=(64, 64)):
        self.resolution = resolution
        self.frame_buffer = []

    def update(self, frame):
        """
        Add a new frame to the buffer and maintain max size.
        """
        self.frame_buffer.append(frame)
        max_buffer_size = 5
        if len(self.frame_buffer) > max_buffer_size:
            self.frame_buffer.pop(0)

    def get_state(self):
        """
        Return the aggregated state of recent frames.
        """
        if not self.frame_buffer:
            return None
        # Simple example: return the latest frame
        return self.frame_buffer[-1]

    def reset(self):
        """
        Clear the frame buffer.
        """
        self.frame_buffer = []
