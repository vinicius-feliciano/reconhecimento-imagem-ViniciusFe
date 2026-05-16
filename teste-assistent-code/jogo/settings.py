# settings.py

# Dimensões da tela
WIDTH = 800
HEIGHT = 600

# Taxa de quadros por segundo
FPS = 60

# Cores (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Configurações do Jogador
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 30
PLAYER_SPEED = 7

# Configurações do Tiro
PROJECTILE_WIDTH = 5
PROJECTILE_HEIGHT = 15
PROJECTILE_SPEED = -10 # Valor negativo para mover para cima

# Configurações do Asteroide
ASTEROID_MIN_SIZE = 20
ASTEROID_MAX_SIZE = 50
ASTEROID_MIN_SPEED = 3
ASTEROID_MAX_SPEED = 7
SPAWN_RATE = 40 # A cada quantos frames um novo asteroide aparece
