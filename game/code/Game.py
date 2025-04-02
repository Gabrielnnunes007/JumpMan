#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from Menu import Menu
class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(600,480))

    def run(self):
        menu = Menu(self.window)
        menu.run()
        pass
