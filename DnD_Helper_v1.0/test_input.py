import unittest
from unittest.mock import patch
from input import InputService

class TestInputService(unittest.TestCase):

    def setUp(self):
        self.input_service = InputService()

    @patch('builtins.input', return_value='10')  # Mock input to always return '10'
    def test_get_int_input_valid(self, mocked_input):
        result = self.input_service.get_int_input("Enter value", default=5, min_val=1, max_val=20)
        self.assertEqual(result, 10)
        mocked_input.assert_called_once_with("Enter value (default 5): ")

    @patch('builtins.input', return_value='25')  # Mock input to return a number out of range
    def test_get_int_input_out_of_range(self, mocked_input):
        result = self.input_service.get_int_input("Enter value", default=10, min_val=1, max_val=20)
        self.assertEqual(result, 10)  # It should revert to default as input is out of range
        mocked_input.assert_called_once_with("Enter value (default 10): ")

    @patch('builtins.input', return_value='abc')  # Mock input to simulate invalid input
    def test_get_int_input_invalid(self, mocked_input):
        result = self.input_service.get_int_input("Enter value", default=10, min_val=1, max_val=20)
        self.assertEqual(result, 10)  # It should revert to default since 'abc' is not an integer
        mocked_input.assert_called_once_with("Enter value (default 10): ")

    @patch('builtins.input', return_value='Warrior')  # Mock input for valid class selection
    def test_get_valid_class_input_valid(self, mocked_input):
        result = self.input_service.get_valid_class_input()
        self.assertEqual(result, 'Warrior')
        mocked_input.assert_called_once_with("Enter character class (Warrior, Wizard): ")

    @patch('builtins.input', return_value='InvalidClass')  # Mock input for invalid class selection
    def test_get_valid_class_input_invalid(self, mocked_input):
        result = self.input_service.get_valid_class_input()
        self.assertEqual(result, 'Warrior')  # Should retry until valid input is received
        mocked_input.assert_called()

if __name__ == '__main__':
    unittest.main()
