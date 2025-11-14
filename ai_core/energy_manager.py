k# ai_core/energy_manager.py

class EnergyManager:
    def __init__(self):
        self.energy = 100

    def consume(self, amount):
        self.energy -= amount

