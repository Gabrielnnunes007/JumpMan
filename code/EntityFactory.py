#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Background import Background
from code.Enemy import Enemy
from code.Player import Player
from code.Const import WIN_WIDTH


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

            case 'Level2bg':
                list_bg = []
                for i in range(2):
                    list_bg.append(Background(f'Level2bg{i}',(0,0)))
                    list_bg.append(Background(f'Level2bg{i}',(WIN_WIDTH,0)))
                return list_bg

            case 'Level3bg':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'Level3bg{i}',(0,0)))
                    list_bg.append(Background(f'Level3bg{i}',(WIN_WIDTH,0)))
                return list_bg

            case 'Level4bg':
                list_bg = []
                for i in range(4):
                    list_bg.append(Background(f'Level4bg{i}',(0,0)))
                    list_bg.append(Background(f'Level4bg{i}',(WIN_WIDTH,0)))
                return list_bg

            case 'Level5bg':
                list_bg = []
                for i in range(4):
                    list_bg.append(Background(f'Level5bg{i}',(0,0)))
                    list_bg.append(Background(f'Level5bg{i}',(WIN_WIDTH,0)))
                return list_bg

            case 'Level6bg':
                list_bg = []
                for i in range(4):
                    list_bg.append(Background(f'Level6bg{i}',(0,0)))
                    list_bg.append(Background(f'Level6bg{i}',(WIN_WIDTH,0)))
                return list_bg


            case 'Player1':
                return Player('Player1', (10,215))
            case 'Player2':
                return Player('Player2', (50,215))
            case 'Enemy1':
                return Enemy('Enemy1', (random.randint(WIN_WIDTH, 600), 225))
            case 'Enemy2':
                return Enemy('Enemy2', (random.randint(WIN_WIDTH, 600), 225))
            case 'Enemy3':
                return Enemy('Enemy3', (random.randint(WIN_WIDTH, 600), 225))
            case 'Enemy4':
                return Enemy('Enemy4', (random.randint(WIN_WIDTH, 600), 225))
            case 'Enemy5':
                return Enemy('Enemy5', (random.randint(WIN_WIDTH, 600), 225))
            case 'Enemy6':
                return Enemy('Enemy6', (random.randint(WIN_WIDTH, 600), 225))