# experiments/data_logging.py

"""
Data Logging Module
Handles structured logging of system states and events for analysis.
"""

import json
from datetime import datetime

class DataLogger:
    def __init__(self, filename="log.json"):
        self.filename = filename
        self.entries = []

    def log(self, data):
        """
        Log a new data entry with timestamp.
        """
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "data": data
        }
        self.entries.append(entry)

    def save(self):
        """
        Save all logged entries to a JSON file.
        """
        with open(self.filename, "w") as f:
            json.dump(self.entries, f, indent=2)

    def reset(self):
        """
        Clear all current log entries.
        """
        self.entries = []
