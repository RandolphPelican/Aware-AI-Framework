# stage3_recursive_closure/closure_loop.py

"""
Recursive Closure Module
Implements self-referential awareness loops for nested AI agents.
"""

class RecursiveClosure:
    def __init__(self, depth=3):
        self.depth = depth
        self.state_stack = []

    def push_state(self, state):
        """
        Add a new state to the stack, maintaining the depth limit.
        """
        self.state_stack.append(state)
        if len(self.state_stack) > self.depth:
            self.state_stack.pop(0)

    def get_current_state(self):
        """
        Return the most recent state.
        """
        if not self.state_stack:
            return None
        return self.state_stack[-1]

    def reset(self):
        """
        Clear all stored states.
        """
        self.state_stack = []
