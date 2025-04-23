from characterClass import Wizard, Fighter

# ----- BUILDER PATTERN -----
class CharacterBuilder:
    def __init__(self):
        self.name = ""
        self.char_class = "Wizard"
        self.history = ""
        self.stats = {"STR": 10, "DEX": 10, "CON": 10, "INT": 10, "WIS": 10, "CHA": 10}
        self.health = 100
        self.inventory = []
        self.abilities = []

    def set_name(self, name):
        self.name = name
        return self

    def set_class(self, char_class):
        self.char_class = char_class
        return self

    def set_history(self, history):
        self.history = history
        return self

    def set_stats(self, stats):
        self.stats = stats
        return self

    def set_health(self, health):
        self.health = health
        return self

    def add_item(self, item):
        self.inventory.append(item)
        return self

    def add_ability(self, ability):
        self.abilities.append(ability)
        return self

    def build(self):
        if self.char_class == "Wizard":
            return Wizard(self.name, self.history, self.stats, self.health, self.inventory, self.abilities)
        elif self.char_class == "Fighter":
            return Fighter(self.name, self.history, self.stats, self.health, self.inventory, self.abilities)
        else:
            raise ValueError("Unknown class")
