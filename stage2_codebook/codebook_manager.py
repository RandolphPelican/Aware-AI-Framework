# stage2_codebook/codebook_manager.py

"""
Codebook Manager Module
Handles storage, retrieval, and consolidation of patterns detected by demodulators.
"""

class CodebookManager:
    def __init__(self):
        self.codebook = {}

    def add_pattern(self, key, pattern):
        """
        Add a pattern to the codebook under a specific key.
        """
        if key not in self.codebook:
            self.codebook[key] = []
        self.codebook[key].append(pattern)

    def get_patterns(self, key):
        """
        Retrieve all patterns associated with a key.
        """
        return self.codebook.get(key, [])

    def consolidate(self):
        """
        Merge patterns into higher-order representations.
        Simple example: average numeric patterns if possible.
        """
        consolidated = {}
        for key, patterns in self.codebook.items():
            if patterns and all(isinstance(p, (int, float)) for p in patterns):
                consolidated[key] = sum(patterns) / len(patterns)
            else:
                consolidated[key] = patterns
        return consolidated

    def reset(self):
        """
        Clear the entire codebook.
        """
        self.codebook = {}
