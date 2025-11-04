k# stage3_recursive_closure/closure_loop.py

"""
Recursive Closure Module
Implements self-referential feedback loops for nested-mind awareness simulation.
"""

class RecursiveClosure:
    def __init__(self, depth=3):
        self.depth = depth
        self.state_stack = []

    def update(self, input_state):
        """
        Push a new state into the stack and maintain closure depth.
        """
        self.state_stack.append(input_state)
        if len(self.state_stack) > self.depth:
            self.state_stack.pop(0)

    def get_state(self):
        """
        Return the current aggregated state of the recursive loop.
        """
        if not self.state_stack:
            return None
        # Simple aggregation: return the most recent state
        return self.state_stack[-1]

    def reset(self):
        """
        Clear all states in the recursive closure loop.
        """
        self.state_stack = []

