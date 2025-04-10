# c
import pygame

color_red = (180,0,0)
color_white =(255,255,255)
color_green = (255,165,0)
color_blue = (0,128,128)

# e
ENTITY_SPEED = {
    'Level1bg0' : 0,
    'Level1bg1' : 1.6,
    'Level1bg2' : 1,
    'Level1bg3' : 1,

    'Level2bg0' : 0,
    'Level2bg1' : 1.6,
    'Level2bg2' : 1,

    'Level3bg0': 0,
    'Level3bg1': 1.6,
    'Level3bg2': 1,
    'Level3bg3': 1,
    'Level3bg4': 1,
    'Level3bg5': 1,
    'Level3bg6': 1,

    'Level4bg0' : 1,
    'Level4bg1' : 1.6,
    'Level4bg2' : 1,
    'Level4bg3' : 1,

    'Level5bg0': 1,
    'Level5bg1': 1.6,
    'Level5bg2': 1,
    'Level5bg3': 1,

    'Level6bg0': 1,
    'Level6bg1': 1.6,
    'Level6bg2': 1,
    'Level6bg3': 1,

    'Player1': 5,
    'Player2': 5,
    'Enemy1': 2,
    'Enemy2': 3,
    'Enemy3': 4,
    'Enemy4': 4,
    'Enemy5': 4,
    'Enemy6': 4,
}
ENTITY_HEALTH = {
    'Level1bg0': 999,
    'Level1bg1': 999,
    'Level1bg2': 999,
    'Level1bg3': 999,

    'Level2bg0': 999,
    'Level2bg1': 999,
    'Level2bg2': 999,

    'Level3bg0': 999,
    'Level3bg1': 999,
    'Level3bg2': 999,
    'Level3bg3': 999,
    'Level3bg4': 999,
    'Level3bg5': 999,
    'Level3bg6': 999,

    'Level4bg0': 999,
    'Level4bg1': 999,
    'Level4bg2': 999,
    'Level4bg3': 999,

    'Level5bg0': 999,
    'Level5bg1': 999,
    'Level5bg2': 999,
    'Level5bg3': 999,

    'Level6bg0': 999,
    'Level6bg1': 999,
    'Level6bg2': 999,
    'Level6bg3': 999,

    'Player1': 300,
    'Player2': 300,
    'Enemy1': 999,
    'Enemy2': 999,
    'Enemy3': 999,
    'Enemy4': 999,
    'Enemy5': 999,
    'Enemy6': 999,
}

ENTITY_DAMAGE = {
    'Level1bg0': 0,
    'Level1bg1': 0,
    'Level1bg2': 0,
    'Level1bg3': 0,

    'Level2bg0': 0,
    'Level2bg1': 0,
    'Level2bg2': 0,

    'Level3bg0': 0,
    'Level3bg1': 0,
    'Level3bg2': 0,
    'Level3bg3': 0,
    'Level3bg4': 0,
    'Level3bg5': 0,
    'Level3bg6': 0,

    'Level4bg0': 0,
    'Level4bg1': 0,
    'Level4bg2': 0,
    'Level4bg3': 0,

    'Level5bg0': 0,
    'Level5bg1': 0,
    'Level5bg2': 0,
    'Level5bg3': 0,

    'Level6bg0': 0,
    'Level6bg1': 0,
    'Level6bg2': 0,
    'Level6bg3': 0,

    'Player1': 1,
    'Player2': 1,
    'Enemy1': 25,
    'Enemy2': 25,
    'Enemy3': 25,
    'Enemy4': 25,
    'Enemy5': 25,
    'Enemy6': 25,
}
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2
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

#t
TIMEOUT_STEP = 100
TIMEOUT_LEVEL = 10000
# w
WIN_WIDTH = 576
WIN_HEIGHT = 324