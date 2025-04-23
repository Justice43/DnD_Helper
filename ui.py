import pygame
from constants import *

class UserInterface:
    def __init__(self):
        
        pygame.init()
        pygame.display.set_caption("D&D Character Creator")
        
        self.WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        self.font = pygame.font.SysFont(None, FONT_SIZE_SMALL)
        
        #Inputs
        self.input_boxes = {
            "name": pygame.Rect(INPUT_LEFT, INPUT_NAME_TOP, INPUT_NAME_WIDTH, INPUT_HEIGHT),
            "history": pygame.Rect(INPUT_LEFT, INPUT_HYSTORY_TOP, INPUT_HISTORY_WIDTH, INPUT_HEIGHT)
        }
        self.inputs = {
            "name": "",
            "history": ""
        }
        
        #Buttons
        self.create_btn = pygame.Rect(*CREATE_BTN_POS, *BUTTON_DIMENSIONS)
        self.class_btn = pygame.Rect(*CLASS_BTN_POS, *BUTTON_DIMENSIONS)

    def draw_text(self, text, position, size=FONT_SIZE_SMALL, color=TEXT_COLOR, align = "center"):
        font = pygame.font.SysFont(None, size)
        text_surface = font.render(text, True, color)

        #Text alignment default - center
        #For buttons
        if isinstance(position, pygame.Rect):
            if align == "center":
                text_rect = text_surface.get_rect(center=position.center)
            elif align == "left":
                text_rect = text_surface.get_rect(midleft=position.midleft)
        #For simple text
        elif isinstance(position, tuple):
            if align == "center":
                text_rect = text_surface.get_rect(center=position)
            elif align == "left":
                text_rect = text_surface.get_rect(topleft=position)

        self.WIN.blit(text_surface, text_rect)

    def draw_button(self, text, rect):
        pygame.draw.rect(self.WIN, LIGHT_BLUE, rect)
        self.draw_text(text, rect)

    #After pressing create button
    def render_character(self, char):
        lines = char.get_info().split('\n')
        y = 300
        for line in lines:
            self.draw_text(line, (50, y), FONT_SIZE_SMALL, align = "left")
            y += 25

    def draw_window(self, inputs, selected_class, character):
        self.WIN.fill(BACKGROUND_COLOR)

        self.draw_text("Enter Name:", (TEXT_MARGIN_LEFT, INPUT_NAME_TOP + 5), align = "left")
        self.draw_text("Enter Backstory:", (TEXT_MARGIN_LEFT, INPUT_HYSTORY_TOP + 5), align = "left")

        for key in self.input_boxes:
            #The 2 means it's just an outline, not a filled rectangle.
            pygame.draw.rect(self.WIN, WHITE, self.input_boxes[key], 2)
            #Renders the text
            txt_surface = self.font.render(inputs[key], True, WHITE)
            #Draws the rendered text inside the input box.
            self.WIN.blit(txt_surface, (self.input_boxes[key].x + 5, self.input_boxes[key].y + 5))

        self.draw_button("Create", self.create_btn)
        self.draw_button(f"Class: {selected_class}", self.class_btn)

        if character:
            self.render_character(character)

        pygame.display.update()