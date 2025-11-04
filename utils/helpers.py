# utils/helpers.py

"""
Helper functions for the Aware AI Framework.
"""

def normalize_frame(frame):
    """
    Normalize input frame values to range [0, 1].
    """
    min_val = min(frame)
    max_val = max(frame)
    if max_val - min_val == 0:
        return frame
    return [(x - min_val) / (max_val - min_val) for x in frame]

def moving_average(buffer):
    """
    Compute the simple moving average of a list of numbers.
    """
    if not buffer:
        return None
    return sum(buffer) / len(buffer)
