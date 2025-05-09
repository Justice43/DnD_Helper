#main.py
from utils import CharacterManager
from input import InputService

if __name__ == "__main__":
    manager = CharacterManager(InputService())
    manager.run()  # Show menu first
