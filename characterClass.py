from character import Character

# ----- POLYMORPHISM -----
class Wizard(Character):
    def use_ability(self):
        if self.get_abilities():
            return f"{self.get_name()} casts {self.get_abilities()[0]}"
        return f"{self.get_name()} has no spells."


class Fighter(Character):
    def use_ability(self):
        if self.get_abilities():
            return f"{self.get_name()} performs a mighty {self.get_abilities()[0]}"
        return f"{self.get_name()} has no combat skills."