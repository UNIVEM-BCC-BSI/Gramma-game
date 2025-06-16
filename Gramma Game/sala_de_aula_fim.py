import os
import pygame
import sys

def resource_path(relative_path):
    """Retorna o caminho absoluto para o recurso, funcionando no PyInstaller e no modo normal."""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

def main(window, LARGURA, ALTURA):
    """Função principal do cenário da sala de aula (fim)."""

    # Fontes
    CAMINHO_FONTE = resource_path("FONTE/Grand9K_Pixel.ttf")
    fonte = pygame.font.Font(CAMINHO_FONTE, 17)

    indice_dialogo = 0

    # Diálogos
    dialogo = [
        "Uma luz forte brilha... tudo ao seu redor começa a \ndesaparecer. Os dinossauros, as pirâmides, os deuses \ngregos, os arranha-céus, os samurais, os robôs... \nTudo some.",
        "Professora: Acorda! Sonhando com dinossauros de novo? \nSe estava prestando atenção, me diga então...",
        "Professora (voz séria)",
        "What would have happened if the dinosaurs had never \ngone extinct?",
        "Você sorri, respira fundo... e se lembra do que aprendeu \nem Wordcan.",
        "Você (decidido): “They would have continued to dominate \nthe Earth.",
        "Professora (surpresa): “Hmmm... muito bem. Parece que \naprendeu alguma coisa mesmo.”"
    ]

    # Carregamento de imagens
    cenario = pygame.transform.scale(
        pygame.image.load(resource_path("CENARIOS E PERSONAGENS/CENARIO - SALA DE AULA.png")),
        (LARGURA, ALTURA)
    )

    # Função auxiliar
    def renderizar_texto_multilinha(texto, fonte, cor, x, y):
        linhas = texto.split('\n')
        for i, linha in enumerate(linhas):
            texto_surface = fonte.render(linha, True, cor)
            window.blit(texto_surface, (x, y + i * 35))
        # Exibe "Aperte [ENTER]" se o diálogo for pequeno (até 6 linhas)
        if len(linhas) <= 6:
            dica_surface = fonte.render("Aperte [ENTER]", True, cor)
            window.blit(dica_surface, (x, y + (len(linhas) + 1) * 27))

    proximo_cenario = False
    loop = True
    while loop:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                return "sair"
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_RETURN:
                    indice_dialogo = min(indice_dialogo + 1, len(dialogo) - 1)
                    if indice_dialogo == len(dialogo) - 1:
                        proximo_cenario = True
                        loop = False

        window.blit(cenario, (0, 0))
        renderizar_texto_multilinha(dialogo[indice_dialogo], fonte, BRANCO, 180, 50)
        pygame.display.update()

    if proximo_cenario:
        return "tela_de_creditos"
    else:
        return "sair"

    pygame.init()
    pygame.font.init()
    LARGURA, ALTURA = 1280, 720
    window = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Sala de aula")

    proxima_tela = main(window, LARGURA, ALTURA)

    if proxima_tela == "tela_de_creditos":
        import tela_de_creditos
        tela_de_creditos.main()
    pygame.quit()
    sys.exit()

