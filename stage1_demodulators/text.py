# stage1_demodulators/text.py

"""
Text Demodulator Module
Processes linguistic inputs and extracts structured semantic features.
"""

class TextDemodulator:
    def __init__(self):
        self.buffer = []
        self.max_buffer_size = 10

    def update(self, text):
        """
        Add a new text input to the buffer.
        """
        self.buffer.append(text)
        if len(self.buffer) > self.max_buffer_size:
            self.buffer.pop(0)

    def get_state(self):
        """
        Return a simple aggregated linguistic state.
        Example: recent words or sentence count.
        """
        if not self.buffer:
            return None
        # Combine all buffered text and return word count
        combined = " ".join(self.buffer)
        word_count = len(combined.split())
        return {"entries": len(self.buffer), "word_count": word_count}

    def reset(self):
        """
        Clear all buffered text.
        """
        self.buffer = []
