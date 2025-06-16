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
AZUL = (50, 50, 255)
PRETO = (0, 0, 0)

def main(window, LARGURA, ALTURA):
    """Função principal do cenário da Grécia Antiga."""
    # Fontes
    CAMINHO_FONTE = resource_path("FONTE/Grand9K_Pixel.ttf")
    fonte = pygame.font.Font(CAMINHO_FONTE, 18)
    fonte_vida = pygame.font.Font(CAMINHO_FONTE, 30)

    # Estado do jogo
    vida = 4
    max_vida = 3
    jogador = pygame.Rect(9, 560, 40, 40)
    velocidade = 3
    mostrar_dialogo = False
    mostrar_dialogo2 = False
    game_over = False
    proximo_cenario = False

    # Diálogos e quiz
    dialogos = [
        "Agora, estamos na Grécia antiga, onde caminhamos pelas colinas de Atenas, ouvimos os ecos dos filósofos e admiramos a \ngrandiosidade dos templos dedicados aos deuses imortais. Vamos mergulhar nesse mundo de sabedoria e mitologia enquanto \naprendemos os verbos no passado em inglês! ",
        "Muitos verbos regulares só ganham “-ed” no passado.",
        "Exemplo:",
        "Celebrate - celebrated.",
        "Respect - respected.",
        "Protect - protected",
        "Atenção com verbos irregulares! Eles mudam completamente:",
        "Design - designed (regular)",
        "Fight - fought (irregular)",
        "Lead - led (irregular)",
    ]

    quiz = [
        {
            "pergunta": "1 - Preencha as lacunas:  ___ significa lutaram em inglês.",
            "alternativas": [
                "A) Fight",
                "B) Fought",
                "C) Fighting"
            ],
            "resposta_correta": "B"
        },
        {
            "pergunta": "2 -The Olympic Games ___ an important tradition in Ancient Greece.",
            "alternativas": [
                "A) Are ",
                "B) Was",
                "C) Were"
            ],
            "resposta_correta": "C"
        },
        {
            "pergunta": "3 -  Ancient Greeks ___ their gods with grand ceremonies.",
            "alternativas": [
                "A) Celebrate",
                "B) Celebrated",
                "C) Celebrating"
            ],
            "resposta_correta": "B"
        }
    ]

    indice_dialogo = 0
    indice_quiz = 0
    acertos = 0
    resposta_usuario = ""
    feedback = ""
    mostrar_feedback = False
    botoes_alternativas = []
    resposta_usuario_anterior_correta = False
    indice_quiz_erro = 0
    botao_proximo = None

    # Carregamento de imagens (corrigido para usar resource_path)
    inicial = pygame.transform.scale(pygame.image.load(resource_path("CENARIOS E PERSONAGENS/CENARIO - GRECIA ANTIGA.png")), (1280, 720))
    sprite_size = (170, 250)
    SPRITES = {
        "left": pygame.transform.scale(pygame.image.load(resource_path("CENARIOS E PERSONAGENS/assets/lado_esquerdo.png")), sprite_size),
        "right": pygame.transform.scale(pygame.image.load(resource_path("CENARIOS E PERSONAGENS/assets/lado_direito.png")), sprite_size),
        "up": pygame.transform.scale(pygame.image.load(resource_path("CENARIOS E PERSONAGENS/assets/frente.png")), sprite_size),
        "down": pygame.transform.scale(pygame.image.load(resource_path("CENARIOS E PERSONAGENS/assets/frente.png")), sprite_size)
    }

    npc = pygame.transform.scale(pygame.image.load(resource_path("CENARIOS E PERSONAGENS/NPC.png")), (190, 150))
    boss = pygame.transform.scale(pygame.image.load(resource_path("CENARIOS E PERSONAGENS/BOSS - GRECIA.png")), (450, 350))

    # Funções auxiliares
    def renderizar_texto_multilinha(texto, fonte, cor, x, y):
        linhas = texto.split('\n')
        for i, linha in enumerate(linhas):
            window.blit(fonte.render(linha, True, cor), (x, y + i * 35))
        # Exibe "Aperte ENTER" se o diálogo for pequeno (até 3 linhas)
        if len(linhas) <= 3:
            dica_surface = fonte.render("Aperte [ENTER]", True, cor)
            window.blit(dica_surface, (x, y + (len(linhas) + 1) * 25))

    def verificar_resposta(letra):
        nonlocal resposta_usuario, feedback, acertos, vida, game_over, mostrar_feedback
        nonlocal resposta_usuario_anterior_correta, indice_quiz_erro

        resposta_usuario = letra
        if resposta_usuario == quiz[indice_quiz]["resposta_correta"]:
            feedback = "✔️ Resposta correta!"
            acertos += 1
            mostrar_feedback = True
            resposta_usuario_anterior_correta = True
        else:
            feedback = "❌ Resposta incorreta."
            vida -= 1
            if vida <= 0:
                vida = 0
                game_over = True
            mostrar_feedback = True
            resposta_usuario_anterior_correta = False
            indice_quiz_erro = indice_quiz

    # Classe do jogador
    class Player(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()
            self.images = SPRITES
            self.direction = "down"
            self.image = self.images[self.direction]
            self.rect = self.image.get_rect(topleft=(x, y))
            self.speed = 4

        def update(self, keys):
            if keys[pygame.K_LEFT]:
                self.rect.x -= self.speed
                self.direction = "left"
            elif keys[pygame.K_RIGHT]:
                self.rect.x += self.speed
                self.direction = "right"
            self.image = self.images[self.direction]

    player = Player(10, 470)
    all_sprites = pygame.sprite.Group(player)

    # Loop principal
    proxima_tela = None
    loop = True
    pos_mouse = (0, 0)  # Inicializa pos_mouse fora do loop de eventos
    while loop:
        window.blit(inicial, (0, 0))
        all_sprites.update(pygame.key.get_pressed())
        all_sprites.draw(window)

        for i in range(vida):
            window.blit(fonte_vida.render("❤", True, (255, 0, 0)), (10 + i * 30, 10))

        if player.rect.colliderect(pygame.Rect(260, 550, 150, 150)):
            window.blit(npc, (260, 550))
            window.blit(fonte.render("Aperte E para conversar com ele", True, PRETO), (299, 535))

        window.blit(boss, (850, 380))
        window.blit(fonte.render("Aperte X para conversar com ele", True, PRETO), (950, 365))

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                proxima_tela = "sair"
                loop = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    mostrar_dialogo = not mostrar_dialogo
                elif event.key == pygame.K_RETURN:
                    if mostrar_dialogo:
                        if indice_dialogo < len(dialogos) - 1:
                            indice_dialogo += 1
                        else:
                            mostrar_dialogo = False
                            indice_dialogo = 0
                elif event.key == pygame.K_x:
                    mostrar_dialogo2 = not mostrar_dialogo2
                    indice_quiz = 0
                    acertos = 0
                    mostrar_feedback = False
                    resposta_usuario = ""
                    feedback = ""
                elif mostrar_dialogo2 and not mostrar_feedback:
                    if event.key in [pygame.K_a, pygame.K_b, pygame.K_c]:
                        verificar_resposta(chr(event.key).upper())

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos_mouse = pygame.mouse.get_pos()

        if mostrar_dialogo2 and not mostrar_feedback:
            for botao, letra in botoes_alternativas:
                if botao.collidepoint(pos_mouse):
                    verificar_resposta(letra)
        elif mostrar_feedback and botao_proximo and botao_proximo.collidepoint(pos_mouse):
            if resposta_usuario_anterior_correta:
                indice_quiz += 1
            if indice_quiz >= len(quiz):
                mostrar_dialogo2 = False
                proximo_cenario = True
                loop = False
            mostrar_feedback = False
            resposta_usuario = ""
            feedback = ""

        if mostrar_dialogo:
            caixa = pygame.Rect(50, ALTURA - 670, LARGURA - 100, 150)
            pygame.draw.rect(window, BRANCO, caixa)
            pygame.draw.rect(window, PRETO, caixa, 5)
            renderizar_texto_multilinha(dialogos[indice_dialogo], fonte, PRETO, caixa.x + 10, caixa.y + 10)

        if mostrar_dialogo2:
            caixa = pygame.Rect(50, ALTURA - 670, LARGURA - 100, 50)
            pygame.draw.rect(window, BRANCO, caixa)
            pygame.draw.rect(window, PRETO, caixa, 5)

            pergunta = quiz[indice_quiz]["pergunta"]
            alternativas = quiz[indice_quiz]["alternativas"]

            renderizar_texto_multilinha(pergunta, fonte, PRETO, caixa.x + 10, caixa.y + 10)

            botoes_alternativas = []
            for i, alt in enumerate(alternativas):
                botao = pygame.Rect(caixa.x + 10, caixa.y + 60 + i * 40, 800, 35)
                pygame.draw.rect(window, BRANCO, botao)
                pygame.draw.rect(window, PRETO, botao, 2)
                window.blit(fonte.render(alt, True, PRETO), (botao.x + 10, botao.y + 5))
                botoes_alternativas.append((botao, alt[0]))

            if mostrar_feedback:
                cor_caixa = (0, 200, 0) if feedback.startswith("✔️") else (255, 0, 0)
                pygame.draw.rect(window, cor_caixa, (caixa.x + 10, caixa.y + 180, 800, 40))
                window.blit(fonte.render(feedback, True, BRANCO), (caixa.x + 20, caixa.y + 190))
                botao_proximo = pygame.Rect(caixa.x + 850, caixa.y + 180, 180, 40)
                pygame.draw.rect(window, (0, 180, 0), botao_proximo)
                pygame.draw.rect(window, PRETO, botao_proximo, 2)
                window.blit(fonte.render("Próxima", True, BRANCO), (botao_proximo.x + 30, botao_proximo.y + 5))
            else:
                botao_proximo = None

        pygame.display.update()

    if game_over:
        proxima_tela = "tela_inicial"
    elif proximo_cenario:
        proxima_tela = "cenario_novayork"
    else:
        proxima_tela = "sair"

    return proxima_tela