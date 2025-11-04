# stage2_codebook/codebook_manager.py

"""
Codebook Manager Module
Handles storage, retrieval, and updating of cross-modal codebooks.
"""

class CodebookManager:
    def __init__(self):
        self.codebooks = {}

    def add_entry(self, key, value):
        """
        Add or update a codebook entry.
        """
        self.codebooks[key] = value

    def get_entry(self, key):
        """
        Retrieve a codebook entry.
        """
        return self.codebooks.get(key, None)

    def remove_entry(self, key):
        """
        Remove a codebook entry if it exists.
        """
        if key in self.codebooks:
            del self.codebooks[key]

    def clear(self):
        """
        Clear all codebooks.
        """
        self.codebooks = {}
