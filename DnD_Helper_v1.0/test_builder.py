import unittest
from builder import CharacterBuilder
from character import Warrior, Wizard

class TestCharacterBuilder(unittest.TestCase):

    def test_create_warrior(self):
        builder = CharacterBuilder()
        warrior = (builder
            .set_name("Thor")
            .set_class("Warrior")
            .set_history("God of Thunder")
            .set_stat("STR", 18)
            .set_stat("DEX", 12)
            .set_health(100)
            .add_item("Hammer")
            .add_ability("Thunder Strike")
            .build()
        )
        self.assertIsInstance(warrior, Warrior)
        self.assertEqual(warrior._name, "Thor")
        self.assertIn("Hammer", warrior._inventory)
        self.assertIn("Thunder Strike", warrior._abilities)

    def test_create_wizard(self):
        builder = CharacterBuilder()
        wizard = (builder
            .set_name("Gandalf")
            .set_class("Wizard")
            .set_history("The Grey")
            .set_stat("INT", 20)
            .set_stat("DEX", 15)
            .set_health(80)
            .add_item("Staff")
            .add_item("Rope")
            .add_ability("Fireball")
            .add_ability("Teleport")
            .build()
        )
        self.assertIsInstance(wizard, Wizard)
        self.assertEqual(wizard._name, "Gandalf")
        self.assertIn("Staff", wizard._inventory)
        self.assertIn("Fireball", wizard._abilities)

    def test_invalid_class(self):
        builder = CharacterBuilder()
        with self.assertRaises(ValueError):
            builder.set_class("InvalidClass").build()

if __name__ == '__main__':
    unittest.main()
