# ai_core/recursive_closure.py

"""
Recursive Closure Module
Implements self-referential loops for nested awareness and state propagation.
"""

class RecursiveClosure:
    def __init__(self):
        self.state_stack = []

    def push_state(self, state):
        """
        Add a new state to the stack.
        """
        self.state_stack.append(state)

    def pop_state(self):
        """
        Remove and return the latest state.
        """
        if self.state_stack:
            return self.state_stack.pop()
        return None

    def get_current_state(self):
        """
        Return the current top state without removing it.
        """
        if self.state_stack:
            return self.state_stack[-1]
        return None

    def reset(self):
        """
        Clear all states.
        """
        self.state_stack = []
