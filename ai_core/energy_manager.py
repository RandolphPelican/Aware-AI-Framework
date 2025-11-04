# ai_core/energy_manager.py

"""
Energy Manager Module
Handles computational resource allocation and energy-subsidy management.
"""

class EnergyManager:
    def __init__(self):
        self.resources = {}
        self.subsidies = {}

    def allocate(self, module_name, amount):
        """
        Allocate energy/resource units to a module.
        """
        self.resources[module_name] = self.resources.get(module_name, 0) + amount

    def consume(self, module_name, amount):
        """
        Consume energy/resource units from a module.
        """
        if module_name in self.resources:
            self.resources[module_name] = max(0, self.resources[module_name] - amount)

    def apply_subsidy(self, module_name, amount):
        """
        Apply an energy subsidy to a module.
        """
        self.subsidies[module_name] = self.subsidies.get(module_name, 0) + amount
        self.allocate(module_name, amount)

    def reset(self):
        """
        Clear all resource and subsidy records.
        """
        self.resources = {}
        self.subsidies = {}
