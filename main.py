import sys
estabilidade = 100
carga_relogio = 50
riqueza = 100
fragmentos = 0
relacao_anya = ""
def mostrar_status (): 
    print(f"STATUS/Vida: {estabilidade}/100 | Carga: {carga_relogio}/100 | Créditos: {riqueza} | Fragmentos: {fragmentos}/3")
    print("\n" + "=" * 55) 

def pedir_escolha (qtd_opcoes):
    while True:
        try:
            escolha = int(input(f"digite sua escolha 1-{qtd_opcoes}: "))
            if 1 <=escolha <=qtd_opcoes:
                return escolha 
            print(f"Opção inválida, digite um número entre 1 e {qtd_opcoes}")
        except ValueError:
            print("Opção inválida, digite apenas números inteiros!")    

def verificar_game_over ():
    global estabilidade
    if estabilidade <=0:
        print("\n GAME OVER! Sua Estabilidade colapsou a zero.") 
        sys.exit()          

def cena_1 ():
    global carga_relogio, estabilidade

    mostrar_status()
    print("---Kaelen acorda no chão do seu laboratório, O reator quântico central no meio da sala está entrando em superaquecimento e ameaça explodir")
    print("\n O que Kaelen deve fazer?")
    print("1) Usar Escudo Temporal (-15 carga)")
    print("2) Contenção manual (-15 estabilidade)")
    escolha = pedir_escolha(2) 
    if escolha == 1:
        carga_relogio -= 15
    else:
        estabilidade -= 15

    verificar_game_over()

def cena_2 ():
    global carga_relogio, estabilidade
    mostrar_status()

    print("--- Kaelen cai em uma metrópole vitoriana dominada por engrenagens Um autômato patrulheiro, corrompido pela matéria escura, ergue seu martelo mecânico e avança contra Kaelen---")
    print("\n Como Kaelen deve enfrentar a ameaça do autômato?")
    print("1) Disparar pulso eletromagnético (-15 carga)")
    print("2) Esquiva rápida para fazer o autômato colidir contra a parede (-10 de Estabilidade +35 carga)")
    escolha = pedir_escolha(2) 
    if escolha == 1:
        carga_relogio -= 15
    else: 
        estabilidade -= 15 
        carga_relogio += 35 

    verificar_game_over()

def cena_3 ():
    global carga_relogio, estabilidade, fragmentos

    mostrar_status()
    print("--- O scanner do relógio aponta que o 1º Fragmento está trancado dentro do cofre blindado da Torre Central de Vapor. Guardas de ferro patrulham o corredor---")
    print("\n Qual estratégia Kaelen utilizará para acessar o cofre?")
    print("1) Hackear Fechadura (-15 de Carga, +1º Fragmento).")
    print("2) Forçar a abertura do mecanismo usando uma alavanca hidráulica encontrada no salão (-15 de Estabilidade, +1º Fragmento).")
    escolha = pedir_escolha(2) 
    if escolha == 1:
        carga_relogio -= 15
    else: 
        estabilidade -= 15 

    fragmentos += 1

    print("\n[🎉] Você obteve o 1º Fragmento de Core!")

    verificar_game_over()

def cena_4 ():
    global carga_relogio, estabilidade
    mostrar_status()

    print("--- A ferrugem tomou a ponte metálica que conecta as torres da cidade, fazendo a estrutura ceder e despencar sobre o abismo de fuligem ---")
    print("\n Como cruzar a ponte em colapso antes que ela caia por completo?")
    print("1) Ativar o salto temporal até a outra extremidade da ponta (-20 carga)")
    print("2)  Disparar em corrida máxima pelos cabos suspensos, arriscando cortes e quedas (-20 de estabilidade)")
    escolha = pedir_escolha(2) 
    if escolha == 1:
        carga_relogio -= 20
    else: 
        estabilidade -= 20 
    print("\n[🎉] Você conseguiu cruzar a ponte com sucesso!")

    verificar_game_over()

def cena_5 ():
    global carga_relogio, estabilidade

    mostrar_status()
    print("---Kaelen alcança o arco no topo da torre, porém o dispositivo está com a energia zerada devido a interferência magnética da cidade ---")
    print("\n O que Kaelen fará para alimentar o portal e abrir a fenda?")
    print("1) Canalizar a energia do relógio de refração para os capacitores do portal (-25 carga")
    print("2) Usar o bio-choque do própio corpo para induzir uma descarga de emergência nos elétrodos (-15 de estabilidade)")
    escolha = pedir_escolha(2) 
    if escolha == 1:
        carga_relogio -= 25
    else:
        estabilidade -= 15

    verificar_game_over()

def cena_6 ():
    global carga_relogio, estabilidade, riqueza

    mostrar_status()
    print("--- Kaelen encontra os restos flutuantes de um satélite de pesquisa temporal abandonado. Ele possui alguns minutos de gravidade estável ---")
    print("\n Em qual sistema do satélite Kaelen deve focar seus esforços de restauração?")
    print("1) Drenar painéis fotovoltaicos para recarregar as baterias do relógio (+35 de Carga)")
    print("2) Usar cápsula médica de emergência para tratar seus ferimentos e queimaduras (+25 de Estabilidade)")
    print("3) Calibrar sensores avançados com suprimentos (-30 Riqueza, +20 Carga, +15 Estabilidade)")
    print("4) Tentar forçar o gerador principal sem cautela (-25 de Estabilidade)")
    escolha = pedir_escolha(4) 
    if escolha == 1:
        carga_relogio += 35
    elif escolha == 2:
        estabilidade += 25
    elif escolha == 3:
        riqueza -= 30
        carga_relogio += 20
        estabilidade += 15
    else:
        estabilidade -= 25

    verificar_game_over()

def cena_7 ():
    global carga_relogio, estabilidade

    mostrar_status()
    print("--- Em um planeta coberto por dunas de vidro e formações cristalinas. Uma tempestade avassaladora de areia corta o ar reduzindo a visibilidade a zero ---")
    print("\n Como Kaelen deve atravessar a tempestade cristalina?")
    print("1) Projetar uma bolha de desaceleração temporal para repelir os grãos de vidro no ar (- 5 de Carga)")
    print("2) Proteger o rosto com panos reforçados e avançar a pé enfrentando o vento cortante (-15 de Estabilidade)")
    escolha = pedir_escolha(2) 
    if escolha == 1:
        carga_relogio -= 5
    else:
        estabilidade -= 15

    verificar_game_over()

def cena_8 ():
    global carga_relogio, estabilidade, fragmentos, riqueza

    mostrar_status()
    print("--- Kaelen encontra uma jovem sobrevivente e habilidosa chamada Anya, cercada por saqueadores temporais. ---")
    print("\n Como ajudar Anya?")
    print("1) Usar frequência do relógio para afugentar os saqueadores (-20 Carga, salva Anya, +2º Fragmento)")
    print("2) Lutar corpo a corpo ao lado dela (-20 Estabilidade, salva Anya, +2º Fragmento)")
    print("3) Pagar o resgate aos saqueadores (-30 Riqueza, salva Anya de forma limpa, +2º Fragmento)")
    escolha = pedir_escolha(3) 
    if escolha == 1:
        carga_relogio -= 20
    elif escolha == 2:
        estabilidade -= 20
    else:
        riqueza -= 30
    fragmentos += 1
    print("\n[🎉] Você obteve o 2º Fragmento de Core")

    verificar_game_over()

def cena_9 ():
    global carga_relogio, estabilidade, relacao_anya

    mostrar_status()
    print("--- Escondidos em uma caverna, Anya cuida dos ferimentos de Kaelen e confessa que gosta dele ---")
    print("\n O que Kaelen vai fazer?")
    print("1) Acolher Anya, com reciprocidade")
    print("2) Manter o foco na missão e continuar como aliados, sem envolvimento romântico")
    escolha = pedir_escolha(2) 
    if escolha == 1:
        relacao_anya = "romance"
        print("\n [❤️] Um laço afetivo mais profundo se formou entre vocês.")
    else:
        relacao_anya = "amizade"
        print("\n [🤝] Vocês reforçaram o pacto de aliança tática como grandes parceiros.")

    verificar_game_over()

def cena_10 ():
    global carga_relogio, estabilidade, riqueza

    mostrar_status()
    print("--- Kaelen encontra uma antiga base subterrânea de mineração temporal. A energia do local é fraca, mas alguns terminais ainda funcionam ---")
    print("\n Qual recurso Kaelen decide extrair do terminal da base?")
    print("1) Conectar o Relógio ao reator auxiliar da base para absorver energia residual (+30 de Carga)")
    print("2) Aplicar um regenerador sintético de tecidos encontrado no kit de socorro (+25 de Estabilidade)")
    print("3) Modificar os equipamentos de Anya para combate (-50 Riqueza)")
    escolha = pedir_escolha(3) 
    if escolha == 1:
        carga_relogio += 30
    elif escolha == 2:
        estabilidade += 25
    else:
        riqueza -= 50

    verificar_game_over()

def cena_11 ():
    global carga_relogio, estabilidade, riqueza

    mostrar_status()
    print("--- O portal seguinte arremessa Kaelen em um vácuo orbital ---")
    print("\n Como Kaelen se locomove entre os escombros flutuantes?")
    print("1) Comprar recarga quântica (+35 Carga, -30 Riqueza)")
    print("2) Escalando com traje especial (+30 Estabilidade, -30 Riqueza)")
    escolha = pedir_escolha(2) 
    if escolha == 1:
        carga_relogio += 35
        riqueza -= 30
    else:
        estabilidade += 30
        riqueza -= 30

    verificar_game_over()

def cena_12 ():
    global carga_relogio, estabilidade, riqueza

    mostrar_status()
    print("--- No centro do vórtice, os leitores do relógio revelam o segredo: o 3º Fragmento não é um objeto, mas a energia que mantém Anya viva! ---")
    print("\n Como extrair o último Fragmento da atração gravitacional?")
    print("1) Analisar a energia do núcleo no peito de Anya (-15 Carga)")
    print("2)  Proteger Anya da radiação com seu próprio corpo (-20 Estabilidade)")
    print("3) Usar um escaneador médico para tentar isolar o sinal (-10 Riqueza)")
    escolha = pedir_escolha(3) 
    if escolha == 1:
        carga_relogio -= 15
    elif escolha == 2:
        estabilidade -= 20
    else:
        riqueza -= 10

    verificar_game_over()

def cena_13 ():
    global carga_relogio, estabilidade

    mostrar_status()
    print("--- Após resgatar o último núcleo, o Relógio de Refracção, Os circuitos quânticos estão superaquecidos e ameaçam derreter o pulso de Kaelen ou pifar definitivamente ---")
    print("\n ")
    print("1) Ejetar capacitores auxiliares (-30 Carga)")
    print("2) Desviar calor para a pele (-20 Estabilidade)")
    escolha = pedir_escolha(2) 
    if escolha == 1:
        carga_relogio -= 30
    else:
        estabilidade -= 20

    verificar_game_over()

def cena_14 ():
    global carga_relogio, estabilidade

    mostrar_status()
    print("--- Kaelen finalmente chega ao epicentro da ameaça: a Cidadela da Ferrugem. No entanto, os portões colossais feitos de metal escuro e espinhos temporais estão trancados por correntes de matéria escura ---")
    print("\n Qual a melhor abordagem para abrir passagem pelos portões do Nexo?")
    print("1) Liberar uma descarga de sobrecarga quântica para derreter as travas dos portões (-20 de Carga)")
    print("2) Escalar a estrutura pontiaguda de espinhos metálicos para encontrar uma abertura superior (-15 de Estabilidade)")
    print("3) Usar a estação de Descompressão (+20 carga)")
    escolha = pedir_escolha(3) 
    if escolha == 1:
        carga_relogio -= 20
    elif escolha == 2:
        estabilidade -= 15
    else:
        carga_relogio += 20

    verificar_game_over()

def cena_15 ():
    global carga_relogio, estabilidade

    mostrar_status()
    print("-- No interior da Cidadela, Kaelen se depara com a Entidade da Ferrugem—uma abominação colossal de metal líquido e energia temporal corrompida que consome as linhas do tempo ---")
    print("\n Como Kaelen deve iniciar a batalha contra a Entidade?")
    print("1) Disparar um feixe concentrado de luz quântica diretamente no olho central da Entidade (-20 de Carga)")
    print("2) Pilhar cápsula de suprimentos exposta enquanto Anya distrai o inimigo (+25 estabilidade)")
    escolha = pedir_escolha(2) 
    if escolha == 1:
        carga_relogio -= 20
    else:
        estabilidade += 25

    verificar_game_over()

def cena_16 ():
    global carga_relogio, estabilidade

    mostrar_status()
    print("--- Furiosa, a Entidade ergue seus braços de matéria escura e lança uma onda de choque de distorção temporal ---")
    print("\n Como reagir à onda de deterioração que avança na direção de Kaelen?")
    print("1) Rolar para o lado e absorver apenas o impacto parcial da onda de choque no escudo (-20 de Estabilidade)")
    print("2) Absorver o choque com o relógio (+30 carga)")
    escolha = pedir_escolha(2) 
    if escolha == 1:
        estabilidade -= 20
    else:
        carga_relogio += 30

    verificar_game_over()

def cena_17 ():
    global carga_relogio, riqueza

    mostrar_status()
    print("--- Ao defender o ataque, Kaelen percebe que o núcleo biomecânico da Entidade fica exposto por uma fração de segundo no centro do seu peito ---")
    print("\n Qual ataque de oportunidade Kaelen executará?")
    print("1) Executar uma descarga total dos capacitores do relógio diretamente no ponto fraco (-25 de Carga)")
    print("2)Avançar com uma lâmina de plasma improvisada e perfurar o núcleo em um ataque arriscado (-10 de riqueza)")
    escolha = pedir_escolha(2) 
    if escolha == 1:
        carga_relogio -= 25
    else:
        riqueza -= 10

    verificar_game_over()

def cena_18 ():
    global carga_relogio, estabilidade

    mostrar_status()
    print("--- A Entidade cambaleia ferida. É a oportunidade perfeita para utilizar a energia pura dos 3 Fragmentos de Core coletados durante a jornada e encerrar o combate ---")
    print("\n Como canalizar a energia dos Fragmentos de Core?")
    print("1) Conectar os 3 Fragmentos aos circuitos do Relógio de Refracção para disparar um pulso puro (+15 de Carga)")
    print("2) Unir os 3 Fragmentos manualmente com as próprias mãos, suportando a descarga elétrica (+15 de Estabilidade)")
    escolha = pedir_escolha(2) 
    if escolha == 1:
        carga_relogio += 15
    else:
        estabilidade += 15

    verificar_game_over()

def cena_19 ():
    global carga_relogio, estabilidade

    mostrar_status()
    print("--- A Entidade cambaleia ferida, mas libera uma nuvem densa de fumaça de matéria escura que encobre o caminho. Anya avança entre os escombros, apontando para a brecha que se abriu diretamente no núcleo do reator temporal ---")
    print("\n Como Kaelen deve cruzar o corredor em ruínas para alcançar o núcleo do reator a tempo?")
    print("1) Disparar rajadas de pulso temporal para dispersar a fumaça de matéria escura (-5 carga)")
    print("2) Avançar a toda velocidade entre os escombros e suportar os impactos materiais (-5 de estabilidade)")
    escolha = pedir_escolha(2) 
    if escolha == 1:
        carga_relogio -= 5
    else:
        estabilidade -= 5

    verificar_game_over()

def cena_20 ():
    global carga_relogio, estabilidade

    mostrar_status()
    print("--- Com a Entidade derrotada, o tecido do multiverso flutua suspenso no ar. Diante de Kaelen surge a oportunidade final de decidir o destino de todo o espaço-tempo ---")
    print("\n Qual destino Kaelen escolherá para o multiverso?")
    print("1) Extrair o 3º Fragmento do peito de Anya para salvar o multiverso (Levando a morte de Anya e salvando o universo)")
    print("2) Recusar o sacrifício e proteger Anya a qualquer custo")
    print("3) Absorver o poder da Ferrugem para tentar dominar tudo e todos")
    escolha = pedir_escolha(3) 

    exibir_finais(escolha)

    verificar_game_over()

def exibir_finais(escolha):
    global relacao_anya

    print("\n" + "==" * 30)
    print("--- FIM DA JORNADA ---")
    if escolha == 1:
        print("\n FINAL 1: HERÓI SOLITÁRIO")
        print("Com lágrimas nos olhos, Kaelen remove o fragmento de Anya. O multiverso se estabiliza e as linhas temporais são restauradas, mas Kaelen carrega para sempre o peso de ter perdido sua maior companheira.")

    elif escolha == 2:
        if relacao_anya == "romance":
            print("\n FINAL 2A: AMOR NO VAZIO")
            print("Kaelen recusa-se a perder Anya. Ele segura a mão dela enquanto o multiverso se desfaz ao redor deles, e juntos enfrentam o colapso do espaço-tempo, unidos pelo amor que transcende a própria realidade")
        else:
            print("\n FINAL 2B: LEALDADE INABALÁVEL")
            print("Kaelen recusa-se a sacrificar sua melhor parceira de combate Lado a lado, como companheiros imbatíveis, encaram o colapso do universo,leais um ao outro até o último segundo")

    elif escolha == 3:
        print("\n FINAL 3: O NOVO IMPERADOR DA FERRUGEM")
        print("Corrompido pelo poder absoluto, Kaelen absorve a matéria escura Ele salva o multiverso, mas torna-se a própria ameaça que jurou combater, restringindo a liberdade de todas as realidades existentes.")

    print("\n" + "==" * 30)
    print("OBRIGADO POR JOGAR 'A FERRUGEM DO MULTIVERSO'!")
    print("=" * 55)

def jogar():
    print("A ferrugem do multiverso")
    cena_1() 
    cena_2()
    cena_3()
    cena_4()
    cena_5()
    cena_6()
    cena_7()
    cena_8()
    cena_9()
    cena_10()
    cena_11()
    cena_12()
    cena_13()
    cena_14()
    cena_15()
    cena_16()
    cena_17()
    cena_18()
    cena_19()
    cena_20()

if __name__ == "__main__":
    jogar()