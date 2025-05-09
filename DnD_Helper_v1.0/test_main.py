import unittest
from unittest.mock import patch
from main import CharacterManager
from input import InputService

class TestMain(unittest.TestCase):

    @patch.object(CharacterManager, 'run', return_value=None)
    def test_run(self, mock_run):
        manager = CharacterManager(input_service=InputService())
        manager.run()  # This should just test that 'run' gets called

if __name__ == '__main__':
    unittest.main()
