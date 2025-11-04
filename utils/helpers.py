# utils/helpers.py

"""
Utility Helper Functions
Contains reusable helper functions for the Aware-AI-Framework modules.
"""

def normalize_frame(frame):
    """
    Normalize a numeric frame or tensor to range [0, 1].
    """
    if not frame:
        return frame
    min_val = min(frame)
    max_val = max(frame)
    if max_val - min_val == 0:
        return [0 for _ in frame]
    return [(x - min_val) / (max_val - min_val) for x in frame]

def clamp(value, min_value=0, max_value=1):
    """
    Clamp a numeric value to the specified min and max range.
    """
    return max(min_value, min(max_value, value))

def flatten(nested_list):
    """
    Flatten a nested list into a single list.
    """
    return [item for sublist in nested_list for item in sublist]
