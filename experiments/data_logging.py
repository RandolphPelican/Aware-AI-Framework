# experiments/data_logging.py

"""
Data Logging Module
Handles recording, storage, and retrieval of experimental data from various AI modules.
"""

import os
import json
from datetime import datetime

class DataLogger:
    def __init__(self, log_dir="logs"):
        self.log_dir = log_dir
        os.makedirs(self.log_dir, exist_ok=True)

    def log(self, module_name, data):
        """
        Log data from a module into a timestamped JSON file.
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{self.log_dir}/{module_name}_{timestamp}.json"
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    def read_logs(self, module_name):
        """
        Read all logs associated with a given module.
        """
        logs = []
        for file in os.listdir(self.log_dir):
            if file.startswith(module_name) and file.endswith(".json"):
                with open(os.path.join(self.log_dir, file), "r") as f:
                    logs.append(json.load(f))
        return logs
