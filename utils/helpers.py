# utils/helpers.py

"""
Utility Helpers Module
Provides general-purpose helper functions for the Aware AI Framework.
"""

def clamp(value, min_value, max_value):
    """
    Clamp a numeric value between min_value and max_value.
    """
    return max(min_value, min(max_value, value))

def flatten_list(nested_list):
    """
    Flatten a nested list into a single list.
    """
    flat = []
    for item in nested_list:
        if isinstance(item, list):
            flat.extend(flatten_list(item))
        else:
            flat.append(item)
    return flat

def average(values):
    """
    Compute the average of a list of numbers.
    Returns None if the list is empty.
    """
    if not values:
        return None
    return sum(values) / len(values)
