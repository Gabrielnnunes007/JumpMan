#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame.image
import random
from pygame import Surface, Rect
from pygame.font import Font

from game.code.const import WIN_WIDTH, color_red, MENU_OPTION, color_white


class Menu:
    def __init__(self,window):
        self.window = window
        self.surf = pygame.image.load('./asset/fases/4/dead forest.png')
        self.rect = self.surf.get_rect(left=0,top=0)

    def run(self):
        pygame.mixer_music.load('./asset/game songs/menu.mp3')
        pygame.mixer_music.play(-1)

        while True:
            self.window.blit(source=self.surf,dest=self.rect)
            self.menu_text(60, "Jump", color_red, ((WIN_WIDTH / 2), 50))
            self.menu_text(60, "Man", color_red, ((WIN_WIDTH / 2), 110))

            for i in range(len(MENU_OPTION)):
                self.menu_text(20, MENU_OPTION[i], color_white, ((WIN_WIDTH / 2), 200 + 25 * i))


            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()


    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Times New Roman", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        text_rect.center = (
            text_center_pos[0] + random.randint(1, 0),
            text_center_pos[1] + random.randint(-1, 0)
        )
        shadow_surf = text_font.render(text, True, (150, 0, 0)).convert_alpha()
        shadow_rect = shadow_surf.get_rect(center=(text_center_pos[0] + 2, text_center_pos[1] + 2))
        self.window.blit(shadow_surf, shadow_rect)
        self.window.blit(text_surf, text_rect)
        self.window.blit(source=text_surf, dest=text_rect)
