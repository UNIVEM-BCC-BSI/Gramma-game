import os
import sys
import pygame

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def desenhar_botao(window, texto, x, y, largura, altura, cor, cor_texto):
    fonte_botao = pygame.font.Font(resource_path("FONTE/Grand9K_Pixel.ttf"), 35)
    pygame.draw.rect(window, cor, (x, y, largura, altura))
    texto_render = fonte_botao.render(texto, True, cor_texto)
    texto_rect = texto_render.get_rect(center=(x + largura // 2, y + altura // 2))
    window.blit(texto_render, texto_rect)
    return pygame.Rect(x, y, largura, altura)

def main(window, LARGURA, ALTURA):
    BRANCO = (255, 255, 255)
    CINZA = (50, 50, 50)
    AMARELO = (255, 204, 0)
    PRETO = (0, 0, 0)

    fade_img = pygame.Surface((LARGURA, ALTURA)).convert_alpha()
    fade = fade_img.get_rect()
    fade_img.fill((0, 0, 0))

    fonte_titulo = pygame.font.Font(resource_path("FONTE/Grand9K_Pixel.ttf"), 100)
    fundo = pygame.image.load(resource_path("CENARIOS E PERSONAGENS/fundo.png"))
    fundo = pygame.transform.scale(fundo, (LARGURA, ALTURA))

    loop = True
    while loop:
        window.blit(fundo, (0, 0))
        fade_img.set_alpha(0)
        window.blit(fade_img, fade)

        titulo = fonte_titulo.render("GRAMMA GAME", True, AMARELO)
        window.blit(titulo, (LARGURA // 2 - titulo.get_width() // 2, 60))

        botao_iniciar = desenhar_botao(window, "INICIAR", 470, 300, 240, 60, CINZA, BRANCO)
        botao_creditos = desenhar_botao(window, "CRÉDITOS", 470, 380, 240, 60, CINZA, BRANCO)
        botao_sair = desenhar_botao(window, "SAIR", 470, 460, 240, 60, CINZA, BRANCO)

        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                return "sair"
            if events.type == pygame.MOUSEBUTTONUP and events.button == 1:
                if botao_iniciar.collidepoint(events.pos):
                    return "sala_de_aula"
                if botao_creditos.collidepoint(events.pos):
                    return "creditos"
                if botao_sair.collidepoint(events.pos):
                    return "sair"

        pygame.display.update()
