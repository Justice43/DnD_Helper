from abc import ABC, abstractmethod

# ----- ABSTRACTION & ENCAPSULATION -----
class Character(ABC):
    def __init__(self, name, history, stats, health, inventory, abilities):
        self._name = name
        self._history = history
        self._stats = stats
        self._health = health
        self._inventory = inventory
        self._abilities = abilities

    # Getters (encapsulation)
    def get_name(self):
        return self._name

    def get_history(self):
        return self._history

    def get_stats(self):
        return self._stats

    def get_health(self):
        return self._health

    def get_inventory(self):
        return self._inventory

    def get_abilities(self):
        return self._abilities

    # Info string
    def get_info(self):
        return (
            f"Name: {self.get_name()}\n"
            f"Class: {self.__class__.__name__}\n"
            f"History: {self.get_history()}\n"
            f"Stats: {self.get_stats()}\n"
            f"Health: {self.get_health()}\n"
            f"Inventory: {', '.join(self.get_inventory())}\n"
            f"Abilities: {', '.join(self.get_abilities())}"
        )

    @abstractmethod
    def use_ability(self):
        pass


