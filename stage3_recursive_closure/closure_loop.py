# stage3_recursive_closure/closure_loop.py

"""
Recursive Closure Module
Implements self-referential loops for awareness and state propagation.
"""

class RecursiveClosure:
    def __init__(self, max_depth=5):
        self.max_depth = max_depth
        self.state_stack = []

    def push_state(self, state):
        """
        Push a new state onto the stack.
        """
        self.state_stack.append(state)
        if len(self.state_stack) > self.max_depth:
            self.state_stack.pop(0)

    def current_state(self):
        """
        Return the latest state.
        """
        if not self.state_stack:
            return None
        return self.state_stack[-1]

    def reset(self):
        """
        Clear the state stack.
        """
        self.state_stack = []

    def recursive_update(self, func):
        """
        Apply a function recursively over the stack states.
        """
        for i in range(len(self.state_stack)):
            self.state_stack[i] = func(self.state_stack[i])
