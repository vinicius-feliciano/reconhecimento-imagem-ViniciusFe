# sprites.py
import pygame
import random
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Cria a "imagem" da nave como um retângulo simples
        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        # Posição inicial no centro, perto da base
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 20
        self.speed_x = 0

    def update(self):
        self.speed_x = 0
        keys = pygame.key.get_pressed()
        
        # Movimentação pelas setas do teclado
        if keys[pygame.K_LEFT]:
            self.speed_x = -PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.speed_x = PLAYER_SPEED

        self.rect.x += self.speed_x

        # Limitar para que a nave não saia das bordas da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        # Retorna uma nova instância de Projectile na posição atual da nave
        projectile = Projectile(self.rect.centerx, self.rect.top)
        return projectile

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((PROJECTILE_WIDTH, PROJECTILE_HEIGHT))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed_y = PROJECTILE_SPEED

    def update(self):
        # Move o tiro para cima
        self.rect.y += self.speed_y
        
        # Remove o tiro da memória se ele sair pela parte superior da tela
        if self.rect.bottom < 0:
            self.kill()

class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Tamanho e formato aleatório
        size = random.randint(ASTEROID_MIN_SIZE, ASTEROID_MAX_SIZE)
        self.image = pygame.Surface((size, size))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        
        # Nasce em uma posição X aleatória, logo acima do topo da tela
        self.rect.x = random.randint(0, WIDTH - size)
        self.rect.y = random.randint(-100, -40)
        
        # Velocidade aleatória de queda
        self.speed_y = random.randint(ASTEROID_MIN_SPEED, ASTEROID_MAX_SPEED)

    def update(self):
        # Move o asteroide para baixo
        self.rect.y += self.speed_y
        # A remoção do asteroide se ele passar da tela será tratada no game.py
        # para que possamos detectar a condição de Game Over.
