#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key

from game.code.Entity import Entity
from game.code.Const import ENTITY_SPEED, WIN_WIDTH, PLAYER_KEY_UP, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT, WIN_HEIGHT


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.last_hit_time = 0
        self.hit_cooldown = 500
        self.velocity = 0
        self.gravity = 1
        self.jump_strength = -15
        self.ground_level = 235

    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]

        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.bottom < WIN_HEIGHT:
            if self.rect.centery >= self.ground_level:
                self.velocity = self.jump_strength

        self.velocity += self.gravity
        self.rect.centery += self.velocity

        if self.rect.centery >= self.ground_level:
            self.rect.centery = self.ground_level
            self.velocity = 0
