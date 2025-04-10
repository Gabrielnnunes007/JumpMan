import sys
from datetime import datetime

import pygame
from pygame import Surface, Rect, KEYDOWN, K_RETURN, K_BACKSPACE, K_ESCAPE
from pygame.font import Font

from game.code.Const import SCORE_POS, color_green, MENU_OPTION, color_blue
from game.code.DBProxy import DBProxy


class Score:

    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./asset/fases/levels/score.png').convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (576, 324))  # Redimensiona a imagem
        self.rect = self.surf.get_rect()

    def save(self, game_mode:str, player_score: list[int]):
        self.window.blit(source=self.surf, dest=self.rect)
        db_proxy = DBProxy('DBScore')
        name = ''
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(48, 'YOU WIN!!', color_blue, SCORE_POS['Title'])
            text = 'Enter Player 1 name (4 characters):'
            score = player_score[0]
            if game_mode == MENU_OPTION[0]:
                score = player_score[0]
            if game_mode == MENU_OPTION[1]:
                if player_score[0] >= player_score[1]:
                    score = player_score[0]
                    text = 'P1 enter your name (4 characters):'
                else:
                    score = player_score[1]
                    text = 'P2 enter your name (4 characters):'
            self.score_text(20, text, color_blue, SCORE_POS['EnterName'])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and len(name) == 4:
                        db_proxy.save({'name': name, 'score': score, 'date': get_formatted_date()})
                        self.show()
                        return
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 4:
                            name += event.unicode
            self.score_text(20, name, color_blue, SCORE_POS['Name'])
            pygame.display.flip()
            pass


    def show(self):
        self.window.blit(source=self.surf, dest=self.rect)
        self.window.blit(source=self.surf, dest=self.rect)
        self.score_text(48, 'TOP 10 SCORE',color_blue, SCORE_POS['Title'])
        self.score_text(20, 'NAME     SCORE           DATE      ', color_blue, SCORE_POS['Label'])
        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()

        for player_score in list_score:
            id_, name, score, date = player_score
            self.score_text(20, f'{name}     {score:05d}     {date}', color_blue,
                            SCORE_POS[list_score.index(player_score)])
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
            pygame.display.flip()

    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_por:tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text,True,text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_por)
        self.window.blit(source=text_surf,dest=text_rect)


def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%y")
    return f"{current_time} - {current_date}"