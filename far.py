import pygame

# Inicializar o Pygame
pygame.init()

# Configuração da janela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Imagem em Triângulos")

# Cores
BLACK = (0, 0, 0)

# Carregar a imagem
image_path = "imagem.png"  # Substitua pelo caminho do seu arquivo PNG
panorama = pygame.image.load(image_path).convert_alpha()
image_width = panorama.get_width()
image_height = panorama.get_height()

# Verificar se a imagem tem o tamanho esperado
#if image_width != 1024 or image_height != 1024:
    #raise ValueError("A imagem deve ter exatamente 6000px de largura por 600px de altura.")

# Função para desenhar a imagem em forma de triângulos
def draw_triangles(screen, image):
    half_width = screen_width // 2
    for x in range(half_width):
        left_height = int(screen_height * (x / half_width))
        right_height = int(screen_height * ((half_width - x) / half_width))

        # Parte esquerda do triângulo
        src_rect = pygame.Rect(x, 0, 1, left_height)
        dest_rect = pygame.Rect(half_width + x, (screen_height - left_height) // 2, 1, left_height)
        screen.blit(image, dest_rect, src_rect)

        # Parte direita do triângulo
        src_rect = pygame.Rect(image_width - x - 1, 0, 1, right_height)
        dest_rect = pygame.Rect(x, (screen_height - right_height) // 2, 1, right_height)
        screen.blit(image, dest_rect, src_rect)

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Preencher o fundo
    screen.fill(BLACK)

    # Desenhar os triângulos com a imagem
    draw_triangles(screen, panorama)

    # Atualizar a tela
    pygame.display.flip()

# Sair do Pygame
pygame.quit()
