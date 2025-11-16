class CodebookManager:
    def __init__(self):
        self.store = {}

    def add(self, key, value):
        self.store[key] = value

    def get(self, key):
        return self.store.get(key)

    # Add this method
    def merge(self, data_list):
        """
        Simulate merging multiple data dictionaries into one.
        """
        merged = {}
        for data in data_list:
            merged.update(data)
        return merged
