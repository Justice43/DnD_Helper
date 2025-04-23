#Dungeons and Dragons (DND) Helper:
# Develop a digital character sheet creator
# Create/edit characters with name, class, history
# Edit statistics (STR, DEX, CON, INT, WIS, CHA)
# Set up health, inventory, and abilities

import pygame
import sys
from characterBuilder import CharacterBuilder
from constants import *
from ui import UserInterface

def main():
    ui = UserInterface()
    character_classes = ["Wizard", "Fighter"]
    current_class_index = 0
    selected_class = character_classes[current_class_index]
    character = None
    active_box = None
    
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            
            #QUIT
            if event.type == pygame.QUIT:
                run = False
                
            #Mouse button clicks on a button
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                #Checks where was pressed
                #Class button pressed
                if ui.class_btn.collidepoint(event.pos):
                    
                    #ensures i dont go out of bounds %(modulus) lenght of (character_classes)
                    current_class_index = (current_class_index + 1) % len(character_classes)
                    selected_class = character_classes[current_class_index]
                    
                #Create button pressed
                elif ui.create_btn.collidepoint(event.pos):
                    builder = CharacterBuilder()
                    character = (
                        builder
                        .set_name(ui.inputs["name"])
                        .set_class(selected_class)
                        .set_history(ui.inputs["history"])
                        .add_ability("Fireball" if selected_class == "Wizard" else "Power Strike")
                        .build()
                    )

                #Checks which input box was pressed
                for key, box in ui.input_boxes.items():
                    if box.collidepoint(event.pos):
                        active_box = key
                        break
                    else:
                        active_box = None
            #Checks which keyboard button was pressed
            elif event.type == pygame.KEYDOWN and active_box:
                #Backspace
                if event.key == pygame.K_BACKSPACE:
                    ui.inputs[active_box] = ui.inputs[active_box][:-1]
                #Enter
                elif event.key == pygame.K_RETURN:
                    active_box = None
                #Everything else
                else:
                    ui.inputs[active_box] += event.unicode

        ui.draw_window(ui.inputs, selected_class, character)

    pygame.quit()
    sys.exit()

# Only works form this file
if __name__ == "__main__":
    main()