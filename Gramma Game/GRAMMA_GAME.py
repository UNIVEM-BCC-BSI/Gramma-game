import time, pygame, sys

#Tela inicial


pygame.init()

print("GRAMMA GAME")
print("Jogar")
#Inicio sala de aula

nome = input("Digite o seu nome jovem curioso: \n")
print(f"Sala de aula silenciosa, relógio marcando 14h40. A câmera percorre a sala, mostrando colegas atentos, uma professora explicando na lousa, e então foca {nome} encostado na carteira, dormindo profundamente.")
time.sleep(6)
print(f"Em um colégio qualquer, durante mais uma aula de inglês...Enquanto todos tentam aprender, {nome} que... está em outro mundo.")
time.sleep(6)
print("Mas neste sonho, aprender inglês será uma questão de sobrevivência!")

#fase 1 - Dinossauros

print("="*150)
print("Durante toda a aventura, você será acompanhado pelo carinha da dica, um velho estudioso do tempo que aparece em cada cenário para oferecer dicas, ajudar nas batalhas contra os chefes (bosses) e ensinar os segredos dos tempos verbais. Ele carrega um relógio mágico que brilha quando você acerta as respostas!")
time.sleep(5)
print("Sábio das Palavras: Bem-vindo(a), jovem viajante! Você chegou a Wordcan, um lugar onde as palavras têm poder. Para começar sua jornada, você deve aprender a cumprimentar as pessoas! e alguns desses cumprimetos e:\n")
print("-> Hello / Hi significa Olá")
print("-> Hi, how you doing significa Olá, como você vai")
print("-> Good morning para Bom dia")
print("-> Good afternoon para Boa tarde")
print("-> Good evening para Boa noite")
time.sleep(8)
print("Uma terra perdida onde os dinossauros ainda caminham e... falam! Aqui, o passado não é apenas história — ele é a chave para a sobrevivência. Mas antes de enfrentar tiranossauros e decifrar fósseis mágicos, você precisa dominar algo essencial:os verbos no passado em inglês!\n")
time.sleep(5)
print("="*150)
print("Dica")
print("Se a pergunta começa com “Did...”, use o verbo na forma base.")
print("Exemplo: \n Did dinosaurs live in groups? \n ✔️ Yes, they lived in groups.\n ✔️ Yes, they did. \n❌ Yes, they lives.")
time.sleep(5)

#Desafio 1:
print("="*150)
while True:
    print("Qual dessas frases está correta?")
    print(" A) Did the dinosaur ate meat?\n B) Did the dinosaur eats meat?\n C) Did the dinosaur eat meat?")
    resp = input("Digite a respostas -> ").upper()
    if resp == 'C':
        print("Você acertou")
        break
    else:
        ("Tente novamente")
while True:
    print("___ the T-Rex hunt other dinosaurs?")
    print("A) Do \nB) Did \nC) Does  ")
    resp = input("Digite a respostas -> ").upper()
    if resp == 'B':
        print("Você acertou")
        break
    else:
        ("Tente novamente")
print("="*150)
# Parte 2 - egito
print("Sábio das Palavras: Agora, estamos no Egito antigo onde exploramos as terras do Nilo e desvendamos os segredos das pirâmides e aqui, você precisa dominar o uso de 'was' e 'were' ")
print("="*150)
print("Use “was” ou “were” como passado de “is” e “are”")
print("Exemplos")
print("The T-Rex was very big.")
print("The pyramids were incredible structures.")
time.sleep(6)
print("="*150)

#Desafio 2 - egito
while True:
    print("Complete com a forma correta do Simple past:")
    print("O que você responde após a pergunta: “Where were the pyramids built?”")
    print(" They was built in Giza, They were built in Giza, They built in Giza ")
    resp = input("Digite a respostas -> ").upper()
    if resp == 'THEY WERE BUILT IN GIZA':
        print("Você acertou")
        break
    else:
        print("Tente Novamente")
while True:
    print("The pyramids ___ incredible structures of ancient Egypt")
    print(" Was, Were, Are ")
    resp = input("Digite a resposta -> ").upper()
    if resp == 'WERE':
        print("Você acerou")
        break
    else:
        print("Tente Novamente")
while True:
    print("Ancient Egyptians ___ hieroglyphs on temple walls.")
    print("Write, Wrote, Writing")
    resp = input("Digite a sua resposta -> ")
    if resp == 'WROTE':
        print("Você acertou")
        break
    else:
        print("Tente novamente")

#Parte 3 - Grecia antiga

print("="*150)
print("Agora, estamos na Grécia antiga, onde caminhamos pelas colinas de Atenas, ouvimos os ecos dos filósofos e admiramos a grandiosidade dos templos dedicados aos deuses imortais. Vamos mergulhar nesse mundo de sabedoria e mitologia enquanto aprendemos os verbos no passado em inglês!")
print("Dica")    
print("Muitos verbos regulares só ganham “-ed” no passado.")
print("Exemplos:")
print("Celebrate → \n Respect → respected\n Protect → protected")  
print("Atenção com verbos irregulares! Eles mudam completamente:")
print("Design → designed (regular) \nFight → fought \nTeach → taught \nLead → led")
time.sleep(6)
print("="*150)

#Desafio 3 - grecia antiga

while True:
    print("___ significa lutaram em inglês.")
    print("Fight, Fighting, Fought")
    resp = input("Digite a sua resposta -> ")
    if resp == 'FOUGHT':
        print("Você acertou")
        break
    else:
        print("Tente Novamente")
while True:
    print("The Olympic Games ___ an important tradition in Ancient Greece.")
    print(" Were, Was, Are")
    resp = input("Digite a sua resposta ->").upper()
    if resp == 'WERE':
        print("Você acertou")
        break
    else:
        print("Tente Novamente")
while True:
    print("Ancient Greeks ___ their gods with grand ceremonies.")
    print(" Celebrate, Celebrated, Celebrating ")
    resp = input("Digite a sua resposta -> ")
    if resp == 'CELEBRATED':
        print("Você acertou")
        break
    else:
        print("Tente novamente")

#Parte 4 - Nova York

print("="*150)
print("Sábio das Palavras: Bem-vindo(a) à cidade que nunca dorme! Você acaba de chegar em Nova York, um lugar cheio de luzes, arranha-céus e pessoas apressadas. Aqui, usamos o presente simples para falar de rotinas, fatos e hábitos.")
print(" Dica:")
print("Use o verbo sem s para I / You / We / They \nAdicione s para He / She / It")
time.sleep(6)
print("Exemplos:")
print("I walk in Central Park. \nShe visits Times Square. \nThey take the subway every day.")
time.sleep(5)
print("="*150)

#Desafio 4 - Nova york
while True:
    print("Complete a frase:")
    print("People in New York usually ___ fast.")
    print("walk, walks, walking")
    resp = input("Digite a sua resposta -> ").upper()
    if resp == 'WALK':
        print("Você acertou")
        break
    else:
        print("Tente novamente")
while True:
    print("He ___ the subway to work.")
    print("take, takes, taken")
    resp = input("Digite a sua respostas -> ").upper()
    if resp == 'TAKES':
        print("Você acertou")
        break
    else:
        print("Tente Novamente")
while True:
    print("Qual está correta?")
    print("A) She go to the museum. \nB) She goes to the museum. \nC) She going to the museum. ")
    resp = input("Digite a sua resposta -> ").upper()
    if resp == 'B':
        print("Você acertou")
        break
    else:
        print("tente Novamente")
print("="*150)

#Parte 5 - japão
print("Sábio das Palavras: Agora, estamos no Japão — terra de templos, tecnologia e tradições.Aqui, você verá que a rotina é muito valorizada. Vamos praticar o presente simples com verbos que mostram ações do dia a dia.")
print(" Dica:")
print("Use “do” para perguntas com I, you, we, they.\n Use “does” para he, she, it.")
print("Exemplos:")
print("Do you eat sushi? \nDoes she watch anime? \nThey practice martial arts.")
print("="*150)

#Desafio 5 - Japão

while True:
    print("Qual dessas perguntas está correta?")
    print("A) Do she like ramen? \nB) Does she like ramen? \nC) Does she likes ramen? ")
    resp = input("Digite a sua resposta ->")
    if resp == 'B':
        print("Você acetou")
        break
    else:
        print("Tente novamente")
while True:
    print("Japanese students ___ uniforms at school.")
    print(" wear, wears wearing ")
    resp = input("Digite a sua resposta -> ")
    if resp == 'WEAR':
        print("Você acertou")
        break
    else:
        print("Tente Novamente")
print("="*150)

#Parte 6 - Paris

print("Sábio das Palavras: Chegamos a Paris, cidade do amor, da arte e da língua elegante. Aqui, falamos sobre o que as pessoas gostam, fazem e veem no presente!")
print("Dica:")
print("Use “don’t” para negar com I, you, we, they. \nUse “doesn’t” para he, she, it.")
print("Exemplos:")
print("I don’t speak French very well.\n She doesn’t like coffee. \nThey visit the Eiffel Tower.")
print("="*150)

#Desafio 6 - Paris

while True:
    print("Complete a frase:")
    print("He ___ like croissants")
    print(" don’t, doesn’t, isn’t")
    resp = input("Digite a sua resposta -> ").upper()
    if resp == "DOESN'T":
        print("Você acertou")
        break
    else:
        print("Tente novamente")
while True:
    print("Tourists often ___ photos at the Eiffel Tower")
    print("take, takes, taking")
    resp = input("Digite a sua resposta ->").upper()
    if resp == 'TAKE':
        print("Você acertou")
        break
    else:
        print("Tente novamente")
while True:
    print("Qual está correta?")
    print("A) They doesn’t live in Paris.\nB) They don’t live in Paris.\nC) They not live in Paris.")
    resp = input("Digite a sua resposta -> ")
    if resp == 'B':
        print("Você acertou")
        break
    else:
        print("Tente novamente")
print("="*150)

#Parte 7 - Apocalipse

print("Sábio das Palavras: A terra está em ruínas… o céu ficou escuro… mas ainda há esperança! No mundo pós-apocalíptico, precisamos prever o que acontecerá — e para isso, usamos o tempo futuro com “will”.")
print("Dica:")
print("will + verbo base = futuro")
print("Exemplos:")
print("I will survive. \nThey will rebuild the world. \nShe will find shelter.")

#Desfio 7 - Apocalipse
print("="*150)
while True:
    print("Complete a frase:")
    print("The survivors ___ rebuild the city.")
    print("will, will be, will to")
    resp = input("Digite a sua resposta -> ").upper()
    if resp == 'WILL':
        print("Você acertou")
        break
    else:
        print("Tente Novamente")
while True:
    print("We ___ find food soon.")
    print(" will, will found, will finding")
    resp = input("Digite a sua resposta -> ").upper()
    if resp == 'WILL':
        print("Você acertou")
        break
    else:
        print("Tente novamente")
while True:
    print("Qual frase está correta?")
    print("A) He will goes alone.\nB) He will go alone. \nC) He will going alone.")
    resp = input("Digite a sua resposta -> ").upper()
    if resp == 'B':
        print("Você acertou")
        break
    else:
        print("Tente novamente")
print("="*150)

#Parte 8 - Cidade futurista

print("Sábio das Palavras: Bem-vindo(a) a NeoLumen, no ano 3000! Carros voadores, robôs inteligentes, e você... está prestes a fazer história.Use o futuro com “will” para imaginar e planejar o que vai acontecer.")
print("Dica:")
print("Use will para decisões, promessas e previsões.")
print("Exemplos:")
print("Robots will help humans.\nYou will learn new technologies.\nThe city will grow even more.")

#Desafio 8 - Cidade futurista

print("="*150)
while True:
    print("Complete a frase:")
    print("She ___ become a famous inventor")
    print("will, will to, will be")
    resp = input("Digite a sua resposta -> ").upper()
    if resp == 'WILL':
        print("Você acertou")
        break
    else:
        ("Tente Novamente")
while True:
    print("People ___ live on Mars one day.")
    print(" will, shall, will are")
    resp = input("Digite a sua resposta -> ")
    if resp == 'WILL':
        print("Digite a sua resposta -> ")
        break
    else:
        print("Tente Novamente")
while True:
    print("Qual dessas frases está correta?")
    print("A) They will creates flying cars.\n B) They will create flying cars. \nC) They will creating flying cars.")
    resp = input("Digite a sua resposta -> ")
    if resp == 'B':
        print("Você acertou")
        break
    else:
        print("Tente novamente")
print("="*150)

#Final

print("Uma luz forte brilha... tudo ao seu redor começa a desaparecer. Os dinossauros, as pirâmides, os deuses gregos, os arranha-céus, os samurais, os robôs... Tudo some.")
time.sleep(5)
print(f"Professora: Acorda, {nome}! Sonhando com dinossauros de novo? Se estava prestando atenção, me diga então...")
time.sleep(5)
print("Professora (voz séria):What would have happened if the dinosaurs had never gone extinct?")
time.sleep(5)
print("A sala fica em silêncio. Todos olham para você.")
time.sleep(5)
print("Você sorri, respira fundo... e se lembra do que aprendeu em Wordcan")
time.sleep(6)
print("Você (decidido): They would have continued to dominate the Earth.")
time.sleep(4)
print("Professora (surpresa): Hmmm... muito bem. Parece que aprendeu alguma coisa mesmo.")
print("="*150)
print("A jornada pode ter sido um sonho... mas o conhecimento, esse é real.")
print("Obrigado por jogar!")

