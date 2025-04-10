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
        LEVEL_SETTINGS = {
            'Level1': {'enemy_interval': 2000, 'timeout_step': 100, 'score_interval': 3000, 'points_per_interval': 10},
            'Level2': {'enemy_interval': 1000, 'timeout_step': 90, 'score_interval': 2000, 'points_per_interval': 20},
            'Level3': {'enemy_interval': 900, 'timeout_step': 80, 'score_interval': 1800, 'points_per_interval': 40},
            'Level4': {'enemy_interval': 800, 'timeout_step': 70, 'score_interval': 1600, 'points_per_interval': 65},
            'Level5': {'enemy_interval': 700, 'timeout_step': 60, 'score_interval': 1400, 'points_per_interval': 80},
            'Level6': {'enemy_interval': 400, 'timeout_step': 40, 'score_interval': 1000, 'points_per_interval': 100}
        }

        if self.name in LEVEL_SETTINGS:
            settings = LEVEL_SETTINGS[self.name]
            pygame.time.set_timer(EVENT_ENEMY, settings['enemy_interval'])
            pygame.time.set_timer(EVENT_TIMEOUT, settings['timeout_step'])

        # Cria Player1 e aplica configurações
        player1 = EntityFactory.get_entity('Player1')
        player1.score = player_score[0]
        player1.score_interval = settings['score_interval']
        player1.points_per_interval = settings['points_per_interval']
        self.entity_list.append(player1)

        # Se for 2 players, cria Player2 e aplica configurações
        if game_mode == MENU_OPTION[2]:
            player2 = EntityFactory.get_entity('Player2')
            player2.score = player_score[1]
            player2.score_interval = settings['score_interval']
            player2.points_per_interval = settings['points_per_interval']
            self.entity_list.append(player2)


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


                    if hasattr(ent, 'update_timed_score') and ent.health > 0:
                        ent.update_timed_score()

                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.name == 'Level6':
                        self.timeout = 9999
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

            if self.name == 'Level6':
                self.level_text(14, f'{self.name} - Timeout: MORTE SÚBITA', color_white, (10, 5))
            else:
                self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000 : .1f}s', color_white, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps() : .0f}', color_white,(10, WIN_HEIGHT - 35))

            pygame.display.flip()
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

    def level_text(self,text_size: int, text:str,text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True,text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])

        self.window.blit(source=text_surf, dest=text_rect)