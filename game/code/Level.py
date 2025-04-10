#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys

import pygame.display
from pygame import Surface, Rect
from pygame.font import Font

from game.code import Entity
from game.code.EntityFactory import EntityFactory
from game.code.EntityMediator import EntityMediator
from game.code.Const import color_white, WIN_HEIGHT, MENU_OPTION, EVENT_ENEMY, color_green, color_red, EVENT_TIMEOUT, \
    TIMEOUT_STEP, TIMEOUT_LEVEL
from game.code.Player import Player


class Level:
    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int]):
        self.window = window
        self.timeout = TIMEOUT_LEVEL
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'bg'))
        player = (EntityFactory.get_entity('Player1'))
        player.score = player_score[0]
        self.entity_list.append(player)
        if game_mode == MENU_OPTION[2]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))
            player = (EntityFactory.get_entity('Player2'))
            player.score = player_score[1]
            self.entity_list.append(player)
        pygame.time.set_timer(EVENT_ENEMY,1000)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)


    def run(self, player_score: list[int]):
        pygame.mixer_music.load(f'./asset/game songs/levelMusic.mp3')
        somMonstro1 = pygame.mixer.Sound('./asset/game songs/monstro1.mp3')
        somMonstro2 = pygame.mixer.Sound('./asset/game songs/monstro2.mp3')
        somMonstro3 = pygame.mixer.Sound('./asset/game songs/monstro3.mp3')
        somMonstro4 = pygame.mixer.Sound('./asset/game songs/monstro4.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)
            current_time = pygame.time.get_ticks()
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if hasattr(ent, 'update_timed_score') and ent.health > 0:
                    ent.update_timed_score()
                if ent.name == 'Player1':
                    self.level_text(14, f'P1 - Health: {ent.health} | Score: {ent.score}', color_green, (10, 25))
                elif ent.name == 'Player2':
                    self.level_text(14, f'P2 - Health: {ent.health} | Score: {ent.score}', color_red, (10, 45))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == EVENT_ENEMY:
                    enemies_by_level = {
                        'Level1': ['Enemy1', ],
                        'Level2': ['Enemy1', 'Enemy2',],
                        'Level3': ['Enemy1', 'Enemy2', 'Enemy3'],
                        'Level4': ['Enemy1', 'Enemy2', 'Enemy3','Enemy4'],
                        'Level5': ['Enemy1', 'Enemy2', 'Enemy3''Enemy4','Enemy5'],
                        'Level6': ['Enemy1', 'Enemy2', 'Enemy3','Enemy4','Enemy5','Enemy6']
                    }

                    if self.name in enemies_by_level:
                        choice = random.choice(enemies_by_level[self.name])
                        if enemy := EntityFactory.get_entity(choice):
                            self.entity_list.append(enemy)

                    som_aleatorio = random.choice((somMonstro1, somMonstro2, somMonstro3, somMonstro4))
                    som_aleatorio.set_volume(0.1)
                    som_aleatorio.play()

                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout == 0:
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'Player1':
                                player_score[0] = ent.score
                            if isinstance(ent, Player) and ent.name == 'Player2':
                                player_score[1] = ent.score
                        return True

                found_player = False
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        found_player = True

                if not found_player:
                    return False

            self.level_text(14,f'{self.name} - Timeout: {self.timeout / 1000 : .1f}s', color_white,(10,5))
            self.level_text(14, f'fps: {clock.get_fps() : .0f}', color_white,(10, WIN_HEIGHT - 35))

            pygame.display.flip()
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

    def level_text(self,text_size: int, text:str,text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True,text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])

        self.window.blit(source=text_surf, dest=text_rect)