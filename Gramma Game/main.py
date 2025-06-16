import pygame
import sys
import tela_inicial
import tela_de_creditos
import sala_de_aula
import cenario_dinossauro1
import cenario_egito
import cenario_grecia
import cenario_novayork
import cenario_japao
import cenario_paris
import cenario_apocalipse
import cenario_futurista
import sala_de_aula_fim

# Inicialização do Pygame
pygame.init()
pygame.font.init()

# Definições da janela
LARGURA, ALTURA = 1280, 720
window = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Wordcan")

# Variáveis de controle
proxima_tela = "tela_inicial"

# Função para efeito de fade
def fade(window, color, duration):
    """Realiza um efeito de fade-in/fade-out."""
    for alpha in range(0, 256):
        window.fill(color + (alpha,), special_flags=pygame.BLEND_RGBA_MULT)
        pygame.display.update()
        pygame.time.delay(int(duration / 256))

if __name__ == "__main__":
    while True:
        if proxima_tela == "tela_inicial":
            fade(window, (0, 0, 0), 500)
            proxima_tela = tela_inicial.main(window, LARGURA, ALTURA)
            fade(window, (0, 0, 0), 500)
        elif proxima_tela == "creditos":
            fade(window, (0, 0, 0), 500)
            proxima_tela = tela_de_creditos.main(window, LARGURA, ALTURA)
            fade(window, (0, 0, 0), 500)
        elif proxima_tela == "sala_de_aula":
            fade(window, (0, 0, 0), 500)
            proxima_tela = sala_de_aula.main(window, LARGURA, ALTURA)
            fade(window, (0, 0, 0), 500)
        elif proxima_tela == "cenario_dinossauro1":
            fade(window, (0, 0, 0), 500)
            proxima_tela = cenario_dinossauro1.main(window, LARGURA, ALTURA)
            fade(window, (0, 0, 0), 500)
        elif proxima_tela == "cenario_egito":
            fade(window, (0, 0, 0), 500)
            proxima_tela = cenario_egito.main(window, LARGURA, ALTURA)
            fade(window, (0, 0, 0), 500)
        elif proxima_tela == "cenario_grecia":
            fade(window, (0, 0, 0), 500)
            proxima_tela = cenario_grecia.main(window, LARGURA, ALTURA)
            fade(window, (0, 0, 0), 500)
        elif proxima_tela == "cenario_novayork":
            fade(window, (0, 0, 0), 500)
            proxima_tela = cenario_novayork.main(window, LARGURA, ALTURA)
            fade(window, (0, 0, 0), 500)
        elif proxima_tela == "cenario_japao":
            fade(window, (0, 0, 0), 500)
            proxima_tela = cenario_japao.main(window, LARGURA, ALTURA)
            fade(window, (0, 0, 0), 500)
        elif proxima_tela == "cenario_paris":
            fade(window, (0, 0, 0), 500)
            proxima_tela = cenario_paris.main(window, LARGURA, ALTURA)
            fade(window, (0, 0, 0), 500)
        elif proxima_tela == "cenario_apocalipse":
            fade(window, (0, 0, 0), 500)
            proxima_tela = cenario_apocalipse.main(window, LARGURA, ALTURA)
            fade(window, (0, 0, 0), 500)
        elif proxima_tela == "cenario_futurista":
            fade(window, (0, 0, 0), 500)
            proxima_tela = cenario_futurista.main(window, LARGURA, ALTURA)
            print(f"Após cenario_futurista, proxima_tela = {proxima_tela}") # Adicione esta linha
        elif proxima_tela == "sala_de_aula_fim":
            print("Entrando em sala_de_aula_fim")  # Adicione esta linha
            fade(window, (0, 0, 0), 500)
            proxima_tela = sala_de_aula_fim.main(window, LARGURA, ALTURA)
            fade(window, (0, 0, 0), 500)
            print(f"Após sala_de_aula_fim, proxima_tela = {proxima_tela}") # Adicione esta linha
        elif proxima_tela == "tela_de_creditos":
            fade(window, (0, 0, 0), 500)
            proxima_tela = tela_de_creditos.main(window, LARGURA, ALTURA)
            fade(window, (0, 0, 0), 500)
        elif proxima_tela == "sair":
            pygame.quit()
            sys.exit()