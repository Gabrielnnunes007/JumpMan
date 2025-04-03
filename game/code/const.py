# c
import pygame

color_red = (180,0,0)
color_white =(255,255,255)
color_green = (255,165,0)

# e
ENTITY_SPEED = {
    'Level1bg0' : 0,
    'Level1bg1' : 1.6,
    'Level1bg2' : 1,
    'Level1bg3' : 1,
    'Player1': 5,
    'Player2': 5,
    'Enemy1': 2,
    'Enemy2': 3,
}
EVENT_ENEMY = pygame.USEREVENT + 1

# m
MENU_OPTION = ('NEW GAME ',
               'NEW GAME SURVIVAL',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT'
               )
# p
PLAYER_KEY_UP = {
    'Player1': pygame.K_UP,
    'Player2': pygame.K_w
}

PLAYER_KEY_LEFT = {
    'Player1': pygame.K_LEFT,
    'Player2': pygame.K_a
}
PLAYER_KEY_RIGHT = {
    'Player1': pygame.K_RIGHT,
    'Player2': pygame.K_d
}
PLAYER_KEY_SHOOT = {
    'Player1': pygame.K_RCTRL,
    'Player2': pygame.K_LCTRL
}

# w
WIN_WIDTH = 576
WIN_HEIGHT = 324