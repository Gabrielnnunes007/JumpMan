#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from game.code.Background import Background
from game.code.Enemy import Enemy
from game.code.Player import Player
from game.code.const import WIN_WIDTH


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'Level1bg':
                list_bg = []
                for i in range(4):
                    list_bg.append(Background(f'Level1bg{i}',(0,0)))
                    list_bg.append(Background(f'Level1bg{i}',(WIN_WIDTH,0)))
                return list_bg

            case 'Player1':
                return Player('Player1', (10,215))
            case 'Player2':
                return Player('Player2', (50,215))
            case 'Enemy1':
                return Enemy('Enemy1', (random.randint(WIN_WIDTH, 1000), 225))
            case 'Enemy2':
                return Enemy('Enemy2', (random.randint(WIN_WIDTH, 1000), 225))

