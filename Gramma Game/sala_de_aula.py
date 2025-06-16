import pygame
import sys
import os

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def renderizar_texto_multilinha(window, texto, fonte, cor, x, y):
    linhas = texto.split('\n')
    for i, linha in enumerate(linhas):
        texto_surface = fonte.render(linha, True, cor)
        window.blit(texto_surface, (x, y + i * 35))
    # Exibe "Aperte ENTER" se o diálogo for pequeno (até 3 linhas)
    if len(linhas) <= 6:
        dica_surface = fonte.render("Aperte [ENTER]", True, cor)
        window.blit(dica_surface, (x, y + (len(linhas) + 1) * 26))

def main(window, LARGURA, ALTURA):
    BRANCO = (255, 255, 255)
    PRETO = (0, 0, 0)

    fonte = pygame.font.Font(resource_path("FONTE/Grand9K_Pixel.ttf"), 15)
    cenario = pygame.image.load(resource_path("CENARIOS E PERSONAGENS/CENARIO - SALA DE AULA.png"))
    cenario = pygame.transform.scale(cenario, (LARGURA, ALTURA))

    dialogo = [
        "Sala de aula silenciosa, relógio marcando 14h40.\nOs alunos atentos, a professora explicando\nna lousa, e então um dos alunos\nencosta na carteira, e começa a dormir profundamente.",
        "Em um colégio qualquer, durante mais uma aula \nde inglês... Enquanto todos tentam\n aprender, você... está em outro mundo.",
        "Mas neste sonho, aprender inglês\n será uma questão de sobrevivência!"
    ]
    indice_dialogo = 0

    proximo_cenario = False
    loop = True
    while loop:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                return "sair"
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_RETURN:
                    if indice_dialogo < len(dialogo) - 1:
                        indice_dialogo += 1
                    else:
                        loop = False
                        proximo_cenario = True

        window.blit(cenario, (0, 0))
        renderizar_texto_multilinha(window, dialogo[indice_dialogo], fonte, BRANCO, 180, 50)
        pygame.display.update()

    if proximo_cenario:
        return "cenario_dinossauro1"
    return "sair"


