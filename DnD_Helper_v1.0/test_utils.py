import unittest
from unittest.mock import patch
from utils import CharacterManager
from input import InputService
from character import Warrior, Wizard

class TestCharacterManager(unittest.TestCase):

    @patch.object(InputService, 'get_valid_class_input', return_value="Warrior")
    @patch.object(InputService, 'get_int_input', return_value=10)
    @patch('builtins.input', side_effect=["Thor", "God of Thunder"])
    def test_create_character(self, mock_input, mock_get_int):
        manager = CharacterManager(input_service=InputService())
        character = manager.create_character()
        self.assertIsInstance(character, Warrior)
        self.assertEqual(character._name, "Thor")
        self.assertEqual(character._history, "God of Thunder")

    @patch.object(InputService, 'get_valid_class_input', return_value="Wizard")
    @patch.object(InputService, 'get_int_input', return_value=10)
    @patch('builtins.input', side_effect=["Gandalf", "The Grey"])
    def test_create_wizard(self, mock_input, mock_get_int):
        manager = CharacterManager(input_service=InputService())
        character = manager.create_character()
        self.assertIsInstance(character, Wizard)
        self.assertEqual(character._name, "Gandalf")
        self.assertEqual(character._history, "The Grey")

    @patch('builtins.input', return_value="1")  # Simulate choosing option 1 (Edit stats)
    def test_summary_edit(self, mock_input):
        manager = CharacterManager(input_service=InputService())
        character = Warrior(name="Thor", history="God of Thunder", stats={"STR": 18}, health=100, inventory=[], abilities=[])
        manager.summary(character)  # Will enter the loop and choose edit option

    @patch('builtins.input', return_value="3")  # Simulate saving character
    def test_save_character(self, mock_input):
        manager = CharacterManager(input_service=InputService())
        character = Warrior(name="Thor", history="God of Thunder", stats={"STR": 18}, health=100, inventory=[], abilities=[])
        manager.save_character(character)  # Should save the character to a file

if __name__ == '__main__':
    unittest.main()
