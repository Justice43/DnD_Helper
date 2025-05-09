#utils.py
import json
import sys
from builder import CharacterBuilder
from input import InputService  # Aggregation

class CharacterManager:
    def __init__(self, input_service: InputService):
        self.input_service = input_service  # Aggregation
        self.builder = CharacterBuilder()   # Composition

    def create_character(self):
        self.builder.set_name(input("Enter character name: "))
        self.builder.set_class(self.input_service.get_valid_class_input())
        self.builder.set_history(input("Enter backstory: "))

        for stat in ["STR", "DEX", "CON", "INT", "WIS", "CHA"]:
            self.builder.set_stat(stat, self.input_service.get_int_input(stat, 10, 1, 20))

        self.builder.set_health(self.input_service.get_int_input("Health Points", 100, 1, 9999))

        self.builder.inventory = self._collect("item")
        self.builder.abilities = self._collect("ability")

        return self.builder.build()

    def summary(self, character):
        print("\n--- Character Summary ---")
        character.display()
        print("\n1. Edit stats")
        print("2. Start over")
        print("3. Save")
        print("4. Load")
        print("5. Use special action")
        print("6. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            self.edit_character(character)
        elif choice == "2":
            self.builder = CharacterBuilder()
            character = self.create_character()
            self.summary(character)
        elif choice == "3":
            self.save_character(character)
            self.summary(character)
        elif choice == "4":
            filename = input("File name to load: (Name.json)")
            character = self.load_character(filename)
            if character:
                self.summary(character)
        elif choice == "5":
            if hasattr(character, "special_action"):
                character.special_action()
            else:
                print("This character has no special action.")
            self.summary(character)
        elif choice == "6":
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid choice.")
            self.summary(character)


    def edit_character(self, character):
        for stat in character._stats:
            new_val = self.input_service.get_int_input(f"New {stat}", character._stats[stat], 1, 20)
            character._stats[stat] = new_val
        print("Stats updated.")
        self.summary(character)

    def save_character(self, character):
        filename = f"{character._name}.json"
        data = {
            "_name": character._name,
            "_class_type": character.__class__.__name__,  # Save actual class
            "_history": character._history,
            "_stats": character._stats,
            "_health": character._health,
            "_inventory": character._inventory,
            "_abilities": character._abilities
        }
        try:
            with open(filename, "w") as f:
                json.dump(data, f)
            print(f"Character saved to {filename}")
        except Exception as e:
            print(f"Save failed: {e}")

    def load_character(self, filename):
        try:
            with open(filename, "r") as f:
                data = json.load(f)

            self.builder = CharacterBuilder()
            self.builder.set_name(data["_name"]) \
                        .set_class(data["_class_type"]) \
                        .set_history(data["_history"])

            self.builder.stats = data["_stats"]
            self.builder.health = data["_health"]
            self.builder.inventory = data["_inventory"]
            self.builder.abilities = data["_abilities"]

            character = self.builder.build()
            print(f"\nLoaded character: {character._name}")
            return character

        except Exception as e:
            print(f"Load failed: {e}")
            print("Returning to main menu.")
            return None
        
    def _collect(self, label):
        items = []
        while True:
            val = input(f"Add {label} (or 'done'): ")
            if val.lower() == 'done':
                break
            items.append(val)
        return items
    
    def run(self):
        character = None
        while True:
            print("\n--- DnD Character Manager ---")
            print("1. Create character")
            print("2. Load character")
            print("3. Exit")

            choice = input("Choose an option: ")
            if choice == "1":
                character = self.create_character()
                self.summary(character)
            elif choice == "2":
                filename = input("Enter file name to load: ")
                character = self.load_character(filename)
                if character:
                    self.summary(character)
                else:
                    continue
            elif choice == "3":
                print("Goodbye!")
                sys.exit()
            else:
                print("Invalid choice.")