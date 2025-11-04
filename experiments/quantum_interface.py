k# experiments/quantum_interface.py

"""
Quantum Interface Module
Simulates an interface between AI modules and experimental quantum subsystems.
"""

import random

class QuantumInterface:
    def __init__(self, qubits=4):
        self.qubits = qubits
        self.state = [0] * qubits

    def measure(self):
        """
        Simulate a quantum measurement collapsing the state of each qubit.
        """
        self.state = [random.randint(0, 1) for _ in range(self.qubits)]
        return self.state

    def reset(self):
        """
        Reset all qubits to 0.
        """
        self.state = [0] * self.qubits

    def apply_gate(self, qubit_index, gate):
        """
        Apply a simple gate to a qubit. Only X-gate supported for now (bit flip).
        """
        if gate == "X" and 0 <= qubit_index < self.qubits:
            self.state[qubit_index] ^= 1

