# experiments/data_logging.py

"""
Data Logging Module
Handles structured logging of experimental AI data for analysis and debugging.
"""

import json
import os

class DataLogger:
    def __init__(self, log_file="experiment_log.json"):
        self.log_file = log_file
        self.data = []

    def log(self, entry):
        """
        Add a new entry to the log.
        """
        self.data.append(entry)

    def save(self):
        """
        Save all logged entries to the file in JSON format.
        """
        with open(self.log_file, "w") as f:
            json.dump(self.data, f, indent=4)

    def reset(self):
        """
        Clear the current log data.
        """
        self.data = []
        if os.path.exists(self.log_file):
            os.remove(self.log_file)
