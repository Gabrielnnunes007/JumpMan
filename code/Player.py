#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key

from code.Entity import Entity
from code.Const import ENTITY_SPEED, WIN_WIDTH, PLAYER_KEY_UP, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT, WIN_HEIGHT


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.last_hit_time = 0
        self.score = 0
        self.score_interval = 3000
        self.points_per_interval = 10
        self.last_score_time = pygame.time.get_ticks()
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

    def update_timed_score(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_score_time > self.score_interval:
            self.score += self.points_per_interval
            self.last_score_time = current_time
            return True  # Retorna True se pontos foram adicionados
        return False