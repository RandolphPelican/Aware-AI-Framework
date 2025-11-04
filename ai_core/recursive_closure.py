# ai_core/recursive_closure.py

"""
Recursive Closure Module
Enables self-referential loops and nested-awareness mechanisms.
"""

class RecursiveClosure:
    def __init__(self):
        self.loop_state = []

    def update(self, state):
        """
        Add a new state to the closure loop.
        """
        self.loop_state.append(state)

    def get_state(self):
        """
        Return the current looped state.
        """
        if not self.loop_state:
            return None
        return self.loop_state[-1]

    def reset(self):
        """
        Clear the closure loop state.
        """
        self.loop_state = []
