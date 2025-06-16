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

def main(window, largura, altura):
    """Função principal do cenário de Paris."""

    # Carrega as fontes
    caminho_fonte = resource_path("FONTE/Grand9K_Pixel.ttf")
    fonte = pygame.font.Font(caminho_fonte, 18)
    fonte_vida = pygame.font.Font(caminho_fonte, 30)

    # Define o estado inicial do jogo
    vida = 4
    max_vida = 3
    jogador = pygame.Rect(9, 560, 40, 40)
    velocidade = 3
    exibir_dialogo = False
    exibir_quiz = False
    fim_de_jogo = False
    proximo_cenario = False

    # Define os diálogos
    dialogos = [
        "Sábio das Palavras: Chegamos a Paris, cidade do amor, da arte e da língua elegante. Aqui, falamos sobre o que as pessoas \ngostam, fazem e veem no presente!",
        "Dica\nUse “don’t” para negar com I, you, we, they.\nUse “doesn’t” para he, she, it.",
        "Exemplo:",
        "I don’t speak French very well.",
        "She doesn’t like coffee.",
        "They visit the Eiffel Tower.",
    ]

    # Define o quiz
    quiz = [
        {
            "pergunta": "1 - Complete a frase: He ___ like croissants",
            "alternativas": [
                "A) don’t",
                "B) doesn’t",
                "C) isn’t"
            ],
            "resposta_correta": "B"
        },
        {
            "pergunta": "2 - Tourists often ___ photos at the Eiffel Tower.",
            "alternativas": [
                "A) take ",
                "B) takes",
                "C) taking"
            ],
            "resposta_correta": "A"
        },
        {
            "pergunta": "3 -  Qual está correta?",
            "alternativas": [
                "A) They doesn’t live in Paris",
                "B) They don’t live in Paris.",
                "C) They not live in Paris."
            ],
            "resposta_correta": "B"
        }
    ]

    # Inicializa as variáveis do jogo
    indice_dialogo = 0
    indice_quiz = 0
    acertos = 0
    resposta_usuario = ""
    feedback = ""
    exibir_feedback = False
    botoes_alternativas = []
    resposta_correta_anterior = False
    indice_quiz_erro = 0
    botao_proximo = None

    # Carrega as imagens
    inicial = pygame.transform.scale(pygame.image.load(resource_path("CENARIOS E PERSONAGENS/CENARIO - PARIS.png")), (largura, altura))
    sprite_size = (170, 250)
    sprites = {
        "left": pygame.transform.scale(pygame.image.load(resource_path("CENARIOS E PERSONAGENS/assets/lado_esquerdo.png")), sprite_size),
        "right": pygame.transform.scale(pygame.image.load(resource_path("CENARIOS E PERSONAGENS/assets/lado_direito.png")), sprite_size),
        "up": pygame.transform.scale(pygame.image.load(resource_path("CENARIOS E PERSONAGENS/assets/frente.png")), sprite_size),
        "down": pygame.transform.scale(pygame.image.load(resource_path("CENARIOS E PERSONAGENS/assets/frente.png")), sprite_size)
    }

    npc = pygame.transform.scale(pygame.image.load(resource_path("CENARIOS E PERSONAGENS/NPC.png")), (190, 150))
    boss = pygame.transform.scale(pygame.image.load(resource_path("CENARIOS E PERSONAGENS/BOSS - PARIS.png")), (450, 330))

    # Funções auxiliares
    def renderizar_texto_multilinha(texto, fonte, cor, x, y):
        """Renderiza um texto em várias linhas."""
        linhas = texto.split('\n')
        for i, linha in enumerate(linhas):
            window.blit(fonte.render(linha, True, cor), (x, y + i * 35))
        # Exibe "Aperte ENTER" se o diálogo for pequeno (até 3 linhas)
        if len(linhas) <= 3:
            dica_surface = fonte.render("Aperte [ENTER]", True, cor)
            window.blit(dica_surface, (x, y + (len(linhas) + 1) * 25))

    def verificar_resposta(letra):
        """Verifica se a resposta do usuário está correta."""
        nonlocal resposta_usuario, feedback, acertos, vida, fim_de_jogo, exibir_feedback
        nonlocal resposta_correta_anterior, indice_quiz_erro

        resposta_usuario = letra
        if resposta_usuario == quiz[indice_quiz]["resposta_correta"]:
            feedback = "✔️ Resposta correta!"
            acertos += 1
            exibir_feedback = True
            resposta_correta_anterior = True
        else:
            feedback = "❌ Resposta incorreta."
            vida -= 1
            if vida <= 0:
                vida = 0
                fim_de_jogo = True
            exibir_feedback = True
            resposta_correta_anterior = False
            indice_quiz_erro = indice_quiz

    # Classe do jogador
    class Player(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()
            self.images = sprites
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

    # Cria o jogador
    player = Player(10, 470)
    todos_sprites = pygame.sprite.Group(player)

    # Loop principal
    proxima_tela = None
    executando = True
    pos_mouse = (0, 0)  # Inicializa pos_mouse
    while executando:
        # Desenha o fundo
        window.blit(inicial, (0, 0))

        # Atualiza e desenha os sprites
        todos_sprites.update(pygame.key.get_pressed())
        todos_sprites.draw(window)

        # Desenha a vida do jogador
        for i in range(vida):
            window.blit(fonte_vida.render("❤", True, (255, 0, 0)), (10 + i * 30, 10))

        # Desenha o NPC
        if player.rect.colliderect(pygame.Rect(260, 550, 150, 150)):
            window.blit(npc, (260, 550))
            window.blit(fonte.render("Aperte E para conversar com ele", True, PRETO), (299, 535))

        # Desenha o chefe
        window.blit(boss, (850, 380))
        window.blit(fonte.render("Aperte X para conversar com ele", True, PRETO), (950, 365))

        # Processa os eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                proxima_tela = "sair"
                executando = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    exibir_dialogo = not exibir_dialogo
                elif event.key == pygame.K_RETURN:
                    if exibir_dialogo:
                        if indice_dialogo < len(dialogos) - 1:
                            indice_dialogo += 1
                        else:
                            exibir_dialogo = False
                            indice_dialogo = 0
                elif event.key == pygame.K_x:
                    exibir_quiz = not exibir_quiz
                    indice_quiz = 0
                    acertos = 0
                    exibir_feedback = False
                    resposta_usuario = ""
                    feedback = ""
                elif exibir_quiz and not exibir_feedback:
                    if event.key in [pygame.K_a, pygame.K_b, pygame.K_c]:
                        verificar_resposta(chr(event.key).upper())

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos_mouse = pygame.mouse.get_pos()

        # Lógica de detecção de cliques do mouse
        if exibir_quiz and not exibir_feedback:
            for botao, letra in botoes_alternativas:
                if botao.collidepoint(pos_mouse):
                    verificar_resposta(letra)
        elif exibir_feedback and botao_proximo and botao_proximo.collidepoint(pos_mouse):
            if resposta_correta_anterior:
                indice_quiz += 1
            if indice_quiz >= len(quiz):
                exibir_quiz = False
                proximo_cenario = True
                executando = False
            exibir_feedback = False
            resposta_usuario = ""
            feedback = ""

        # Desenha o diálogo
        if exibir_dialogo:
            caixa = pygame.Rect(50, largura - 670, largura - 100, 150)
            pygame.draw.rect(window, BRANCO, caixa)
            pygame.draw.rect(window, PRETO, caixa, 5)
            renderizar_texto_multilinha(dialogos[indice_dialogo], fonte, PRETO, caixa.x + 10, caixa.y + 10)

        # Desenha o quiz
        if exibir_quiz:
            caixa = pygame.Rect(50, largura - 1200, largura - 100, 49)
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

            if exibir_feedback:
                cor_caixa = (0, 200, 0) if feedback.startswith("✔️") else (255, 0, 0)
                pygame.draw.rect(window, cor_caixa, (caixa.x + 10, caixa.y + 180, 800, 40))
                window.blit(fonte.render(feedback, True, BRANCO), (caixa.x + 20, caixa.y + 190))
                botao_proximo = pygame.Rect(caixa.x + 850, caixa.y + 180, 180, 40)
                pygame.draw.rect(window, (0, 180, 0), botao_proximo)
                pygame.draw.rect(window, PRETO, botao_proximo, 2)
                window.blit(fonte.render("Próxima", True, BRANCO), (botao_proximo.x + 30, botao_proximo.y + 5))
            else:
                botao_proximo = None

        # Atualiza a tela
        pygame.display.update()

    # Define o próximo cenário
    if fim_de_jogo:
        proxima_tela = "tela_inicial"
    elif proximo_cenario:
        proxima_tela = "cenario_apocalipse"
    else:
        proxima_tela = "sair"

    return proxima_tela