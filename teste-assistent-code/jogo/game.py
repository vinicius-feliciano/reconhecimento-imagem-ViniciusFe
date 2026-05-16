# game.py
import pygame
import sys
from settings import *
from sprites import Player, Asteroid, Projectile

# Inicialização do pygame e fonte
pygame.init()
pygame.font.init()

# Configuração da Janela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Atari Space Shooter")
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 32, bold=True)
game_over_font = pygame.font.SysFont("arial", 64, bold=True)

def draw_text(surface, text, font_to_use, color, x, y, center=False):
    text_surface = font_to_use.render(text, True, color)
    text_rect = text_surface.get_rect()
    if center:
        text_rect.center = (x, y)
    else:
        text_rect.topleft = (x, y)
    surface.blit(text_surface, text_rect)

def main():
    # Criação dos grupos de sprites
    all_sprites = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    projectiles = pygame.sprite.Group()

    player = Player()
    all_sprites.add(player)

    score = 0
    running = True
    game_over = False
    spawn_timer = 0

    # Loop Principal
    while running:
        # Define a taxa de quadros (FPS)
        clock.tick(FPS)

        # 1. Processamento de Eventos (Inputs)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if not game_over:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        # O jogador atira e adicionamos o tiro aos grupos correspondentes
                        projectile = player.shoot()
                        all_sprites.add(projectile)
                        projectiles.add(projectile)
            else:
                # Se for Game Over, pressionar Enter reinicia, Esc sai do jogo
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_RETURN:
                        main() # Chama a função principal novamente para reiniciar
                        return

        # 2. Atualização dos Estados e Colisões
        if not game_over:
            all_sprites.update()

            # Lógica para criar novos asteroides em intervalos
            spawn_timer += 1
            if spawn_timer >= SPAWN_RATE:
                spawn_timer = 0
                asteroid = Asteroid()
                all_sprites.add(asteroid)
                asteroids.add(asteroid)

            # Detecta colisão entre tiros (projectiles) e asteroides (asteroids)
            # Ambos os 'True' indicam que tanto o tiro quanto o asteroide serão removidos
            hits = pygame.sprite.groupcollide(asteroids, projectiles, True, True)
            for hit in hits:
                score += 10 # 10 pontos por acerto

            # Detecta colisão entre o jogador e asteroides
            player_hits = pygame.sprite.spritecollide(player, asteroids, False)
            if player_hits:
                game_over = True # Nave atingida!

            # Checa se algum asteroide passou do fundo da tela
            for asteroid in asteroids:
                if asteroid.rect.top > HEIGHT:
                    game_over = True # Asteroide chegou na Terra!

        # 3. Desenho (Renderização)
        screen.fill(BLACK) # Limpa a tela com fundo preto
        all_sprites.draw(screen) # Desenha todos os sprites

        # Desenha a pontuação no canto superior esquerdo
        draw_text(screen, f"Score: {score}", font, WHITE, 10, 10)

        # Desenha a mensagem de fim de jogo se necessário
        if game_over:
            draw_text(screen, "GAME OVER", game_over_font, RED, WIDTH // 2, HEIGHT // 2 - 40, center=True)
            draw_text(screen, "Pressione ENTER para jogar novamente", font, WHITE, WIDTH // 2, HEIGHT // 2 + 30, center=True)

        # Atualiza o display final após todas as modificações
        pygame.display.flip()

    # Finaliza adequadamente
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
