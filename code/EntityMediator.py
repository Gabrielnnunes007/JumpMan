import pygame.mixer

from code.Enemy import Enemy
from code.Entity import Entity
from code.Player import Player


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right <= 0:
                ent.health = 0

    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        valid_interaction = False
        if isinstance(ent1, Player) and isinstance(ent2, Enemy):
            valid_interaction = True
        elif isinstance(ent1, Enemy) and isinstance(ent2, Player):
            valid_interaction = True

        if valid_interaction:  # if valid_interaction == True:
            if (ent1.rect.right >= ent2.rect.left and
                    ent1.rect.left <= ent2.rect.right and
                    ent1.rect.bottom >= ent2.rect.top and
                    ent1.rect.top <= ent2.rect.bottom):
                ent1.health -= ent2.damage


    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    def __give_score():
        pass


    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        current_time = pygame.time.get_ticks()

        # Verifica colisão entre inimigos e jogadores
        if (isinstance(ent1, Enemy) and ent2.name.startswith('Player')) or \
                (isinstance(ent2, Enemy) and ent1.name.startswith('Player')):

            # Determina quem é o jogador
            player = ent1 if ent1.name.startswith('Player') else ent2
            enemy = ent2 if isinstance(ent2, Enemy) else ent1

            if (ent1.rect.right >= ent2.rect.left and
                    ent1.rect.left <= ent2.rect.right and
                    ent1.rect.bottom >= ent2.rect.top and
                    ent1.rect.top <= ent2.rect.bottom):

                # Aplica dano apenas se o cooldown acabou
                if current_time - player.last_hit_time > player.hit_cooldown:
                    player.health -= enemy.damage  # Dano fixo da Const.py
                    player.last_hit_time = current_time
                    print(f"Dano aplicado: {enemy.damage}")  # Debug

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        # Opcional: verifica jogadores mortos
        for ent in entity_list:
            if ent.name.startswith('Player') and ent.health <= 0:
                somMorte = pygame.mixer.Sound('./asset/game songs/morte.mp3')
                somMorte.set_volume(0.3)
                somMorte.play()

        # Filtra e remove automaticamente entidades com health <= 0
        entity_list[:] = [ent for ent in entity_list if ent.health > 0]