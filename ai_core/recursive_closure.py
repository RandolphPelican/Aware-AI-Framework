# ai_core/recursive_closure.py

"""
Recursive Closure Module
Implements self-referential awareness loops for AI agents.
"""

class RecursiveClosure:
    def __init__(self):
        self.state_stack = []

    def push_state(self, state):
        """
        Add a new state to the closure stack.
        """
        self.state_stack.append(state)

    def pop_state(self):
        """
        Remove and return the most recent state.
        """
        if self.state_stack:
            return self.state_stack.pop()
        return None

    def current_state(self):
        """
        Return the current state without removing it.
        """
        if self.state_stack:
            return self.state_stack[-1]
        return None

    def reset(self):
        """
        Clear all states in the stack.
        """
        self.state_stack = []
