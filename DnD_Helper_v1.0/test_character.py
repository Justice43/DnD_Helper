import unittest
from character import Warrior, Wizard

class TestCharacter(unittest.TestCase):
    
    def test_warrior_creation(self):
        warrior = Warrior(name="Thor", history="God of Thunder", stats={"STR": 18, "DEX": 12}, health=100, inventory=["Hammer"], abilities=["Thunder Strike"])
        self.assertEqual(warrior._name, "Thor")
        self.assertEqual(warrior._history, "God of Thunder")
        self.assertEqual(warrior._stats["STR"], 18)
        self.assertEqual(warrior._stats["DEX"], 12)
        self.assertEqual(warrior._health, 100)
        self.assertIn("Hammer", warrior._inventory)
        self.assertIn("Thunder Strike", warrior._abilities)

    def test_warrior_special_action(self):
        warrior = Warrior(name="Thor", history="God of Thunder", stats={"STR": 18, "DEX": 12}, health=100, inventory=["Hammer"], abilities=["Thunder Strike"])
        with self.assertLogs(level='INFO') as log:
            warrior.special_action()
            self.assertIn("charges into battle with a mighty roar!", log.output[0])
    
    def test_wizard_creation(self):
        wizard = Wizard(name="Gandalf", history="The Grey", stats={"INT": 20, "DEX": 15}, health=80, inventory=["Staff", "Rope"], abilities=["Fireball", "Teleport"])
        self.assertEqual(wizard._name, "Gandalf")
        self.assertEqual(wizard._history, "The Grey")
        self.assertEqual(wizard._stats["INT"], 20)
        self.assertEqual(wizard._stats["DEX"], 15)
        self.assertEqual(wizard._health, 80)
        self.assertIn("Staff", wizard._inventory)
        self.assertIn("Fireball", wizard._abilities)

    def test_wizard_special_action(self):
        wizard = Wizard(name="Gandalf", history="The Grey", stats={"INT": 20, "DEX": 15}, health=80, inventory=["Staff", "Rope"], abilities=["Fireball", "Teleport"])
        with self.assertLogs(level='INFO') as log:
            wizard.special_action()
            self.assertIn("casts a devastating arcane spell!", log.output[0])

if __name__ == '__main__':
    unittest.main()
