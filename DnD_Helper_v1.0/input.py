#input.py
class InputService:
    def get_int_input(self, prompt, default=10, min_val=1, max_val=20):
        while True:
            try:
                value = input(f"{prompt} (default {default}): ")
                if not value:
                    return default
                value = int(value)
                if min_val <= value <= max_val:
                    return value
                print(f"Please enter a value between {min_val} and {max_val}.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    def get_valid_class_input(self):
        while True:
            class_input = input("Enter character class (Warrior, Wizard): ").capitalize()
            if class_input in ["Warrior", "Wizard"]:
                return class_input
            print("Invalid class. Please choose 'Warrior' or 'Wizard'.")
