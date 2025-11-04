k# utils/helpers.py

"""
Utility Helper Functions
Contains shared helper functions used across all stages of the Aware AI Framework.
"""

def clamp(value, min_value, max_value):
    """
    Clamp a numeric value between min_value and max_value.
    """
    return max(min_value, min(value, max_value))

def normalize_vector(vector):
    """
    Normalize a numeric vector to unit length.
    """
    magnitude = sum(x**2 for x in vector) ** 0.5
    if magnitude == 0:
        return vector
    return [x / magnitude for x in vector]

def rolling_average(buffer, new_value, max_length=5):
    """
    Maintain a rolling average of the last `max_length` values.
    """
    buffer.append(new_value)
    if len(buffer) > max_length:
        buffer.pop(0)
    return sum(buffer) / len(buffer)

