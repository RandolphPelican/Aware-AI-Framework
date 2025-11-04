# ai_core/energy_manager.py

"""
Energy Manager Module
Manages computational resource allocation and energy subsidies across AI agents.
"""

class EnergyManager:
    def __init__(self, initial_energy=100.0):
        self.energy = initial_energy

    def consume(self, amount):
        """
        Consume a specified amount of energy.
        """
        self.energy = max(self.energy - amount, 0.0)
        return self.energy

    def add(self, amount):
        """
        Add energy to the pool.
        """
        self.energy += amount
        return self.energy

    def status(self):
        """
        Return the current energy level.
        """
        return self.energy
