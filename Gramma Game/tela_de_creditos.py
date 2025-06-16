import sys
import os
import pygame

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def main(window, LARGURA, ALTURA):
    BRANCO = (255, 255, 255)
    PRETO = (0, 0, 0)

    CAMINHO_FONTE = resource_path("FONTE/Grand9K_Pixel.ttf")
    fonte = pygame.font.Font(CAMINHO_FONTE, 22)
    fonte1 = pygame.font.Font(CAMINHO_FONTE, 28)
    fonte_titulo = pygame.font.Font(CAMINHO_FONTE, 36)

    creditos = [
        "Jogo Educacional - GRAMMA GAME",
        "",
        "Desenvolvido por:",
        "Arthur Rossi",
        "Ryan Oliveira",
        "Kaike Remolli",
        "",
        "Roteiro e Design:",
        "Imagens e personagens feitos por IA",
        "Arthur Rossi",
        "Ryan Oliveira",
        "Kaike Remolli",
        "",
        "Equipe de Desenvolvimento",
        "Arthur Rossi",
        "Ryan Oliveira",
        "Kaike Remolli",
        "",
        "Ferramentas Utilizadas:",
        "Python, Pygame, IA",
        "",
        "Agradecimentos Especiais:",
        "Aos nossos professores",
        "A nossa faculdade univem",
        "Obrigado por jogar!",
    ]

    y_pos = ALTURA
    clock = pygame.time.Clock()
    rodando = True

    def desenhar_botao():
        botao_rect = pygame.Rect(20, ALTURA - 60, 120, 40)
        pygame.draw.rect(window, (200, 200, 200), botao_rect)
        texto = fonte.render("Voltar", True, PRETO)
        window.blit(texto, (botao_rect.x + 20, botao_rect.y + 5))
        return botao_rect

    while rodando:
        window.fill(PRETO)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1 and desenhar_botao().collidepoint(evento.pos):
                    rodando = False

        # Desenha os créditos com rolagem
        for i, linha in enumerate(creditos):
            cor = BRANCO
            texto = fonte_titulo.render(linha, True, cor) if i == 0 else fonte1.render(linha, True, cor)
            window.blit(texto, (LARGURA // 2 - texto.get_width() // 2, y_pos + i * 40))

        y_pos -= 1  # Velocidade da rolagem
        if y_pos < -len(creditos) * 40:
            y_pos = ALTURA  # Reinicia rolagem

        desenhar_botao()
        pygame.display.flip()
        clock.tick(60)

    return "tela_inicial"