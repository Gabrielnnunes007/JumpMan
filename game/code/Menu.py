#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame.image
from pygame.font import Font
from game.code.const import WIN_WIDTH, MENU_OPTION, color_white, color_green

class Menu:
    def __init__(self,window):
        self.window = window
        self.surf = pygame.image.load('./asset/fases/levels/menu.png').convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (576, 324))  # Redimensiona a imagem
        self.rect = self.surf.get_rect()

    def run(self):
        menu_option = 0
        pygame.mixer_music.load('./asset/game songs/menu.mp3')
        pygame.mixer_music.set_volume(0.5)
        pygame.mixer_music.play(-1)

        while True:
            self.window.blit(source=self.surf,dest=self.rect)
            self.menu_text(60, "Magical", color_white, ((WIN_WIDTH / 2), 50))
            self.menu_text(60, "Forest", color_green, ((WIN_WIDTH / 2), 110))


            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(30, MENU_OPTION[i], color_white, ((WIN_WIDTH / 2), 200 + 25 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], color_green, ((WIN_WIDTH / 2), 200 + 25 * i))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                somMenu = pygame.mixer.Sound('./asset/game songs/somMenu.mp3')
                somMenu.set_volume(0.3)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            somMenu.play()
                            menu_option += 1
                        else:
                            menu_option = 0
                            somMenu.play()
                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option += -1
                            somMenu.play()
                        else:
                            menu_option = len(MENU_OPTION) -1
                            somMenu.play()
                    if event.key == pygame.K_RETURN:
                        somMenu.play()
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple,
                                text_center_pos: tuple, shadow_color=(50, 50, 50),
                                shadow_offset=2, bold=True):
        text_font = pygame.font.SysFont("Times New Roman", text_size, bold=bold)
        shadow_surf = text_font.render(text, True, shadow_color).convert_alpha()
        shadow_rect = shadow_surf.get_rect(center=(text_center_pos[0] + shadow_offset, text_center_pos[1] + shadow_offset))
        text_surf = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(shadow_surf, shadow_rect)
        self.window.blit(text_surf, text_rect)
