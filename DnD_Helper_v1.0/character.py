#character.py
from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, name, history, stats, health, inventory, abilities):
        self._name = name
        self._history = history
        self._stats = stats
        self._health = health
        self._inventory = inventory
        self._abilities = abilities

    def display(self):
        print(f"\n{self.__class__.__name__} — {self._name}")
        print(f"Backstory: {self._history}")
        print(f"Health: {self._health}")
        print("Stats:")
        for stat, value in self._stats.items():
            print(f"  {stat}: {value}")
        print(f"Inventory: {', '.join(self._inventory) if self._inventory else 'None'}")
        print(f"Abilities: {', '.join(self._abilities) if self._abilities else 'None'}")

    @abstractmethod
    def special_action(self):
        pass


class Warrior(Character):
    def __init__(self, name, history, stats, health, inventory, abilities=None):
        abilities = abilities or ["Power Strike", "Shield Block"]
        super().__init__(name, history, stats, health, inventory, abilities)

    def special_action(self):
        print(f"\n{self._name} charges into battle with a mighty roar!")


class Wizard(Character):
    def __init__(self, name, history, stats, health, inventory, abilities=None):
        abilities = abilities or ["Fireball", "Heal"]
        super().__init__(name, history, stats, health, inventory, abilities)

    def special_action(self):
        print(f"\n{self._name} casts a devastating arcane spell!")

