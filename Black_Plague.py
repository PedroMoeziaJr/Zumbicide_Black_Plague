def zombicide_jogo():
    while True:
        print("\nBem-vindo ao Zombicide: Black Plague")
        print("Escolha uma fase do jogo para receber instruções:")
        print("1. Fase dos Jogadores")
        print("2. Fase dos Zumbis")
        print("3. Sair")
        
        escolha = input("\nDigite sua escolha (1-3): ")

        if escolha == "1":
            print("\nFase dos Jogadores:")
            print("1. Mover de uma zona para outra")
            print("2. Procurar (se não houver zumbi)")
            print("3. Abrir porta")
            print("4. Reorganizar/Trocar item")
            print("5. Atacar")
            print("6. Pegar ou ativar um objeto")
            print("7. Fazer barulho")
            print("8. Não fazer nada.")
            print("9. Voltar")
            opcao_jogador = input("\nEscolha uma ação (1-4): ")

            if opcao_jogador == "1":
                print("\nMover de uma zona para outra:")
                print("\nSe tiver zumbi na sua zona gaste uma ação extra para cada zumbi na zona")
                print("Se a ação de mover parar em uma zona com zumbi a ação acaba independentemente de qualquer coisa.")
            elif opcao_jogador == "2":
                print("\nProcurar (se não houver zumbi):")
                print("\nCompra uma carta e coloca no inventário ou descarta(descarte não conta como ação.")
                print("Se não tiver zumbi na zona pode comprar uma carta de equipamento, equipa ou descarta")
                print("Só pode uma vez por Turno, mesmo que extra grátis")
            
            elif opcao_jogador == "3":
                print("\nAbrir porta:")
                print("Tem que ter arma pra isso")
                print("Veja se tem que rolar dado, valor igual ou maior que a precisao.")
                print("Veja quantidade de dados.")
                print("Abriu a porta? Revele um zumbi de cada zona.")
                print("Construção que começa aberta no inicio do jogo nao tem zumbi.")
                print("Zona da Cripta quando revelada não tem zumbi")

            elif opcao_jogador == "4":
                print("\nReorganizar/Troca item")
                print("Custo de uma ação troque itens SE tiverem na mesma zona, o outro reorganiza livremente")

            elif opcao_jogador == "5":
                print("\nAtacar Zumbi")
                print("Verificar na carta 1- Alcance 2-Quantidade de dados 3-Numero para acertar nos dados 4-Nº de mortes por acerto, E se faz barulho")
                print(" Duas armas idênticas portadas, o jogador pode rolar o dobro de dados com se fosse UMA AÇÃO")
                print("Cada dado acertado(causa 1 de dano) mata um: LERDO, CORREDOR e NECROMANTE.")
                print("BALOFOS só morrem com 2 de dano de uma vez só, ou seja armas com 2 de danos pra cima")
                print("ABOMINAÇÕES só morrem com 3 de dano, ou seja, com FOGO DO DRAGÃO ou com Samsom arma corpo a corpo 2 de dano + Habilidade +1 Dano corpo a corpo")
                print("Se tiver vários zumbis, morrem nessa ordem: 1-LERDO, 2- Balodo ou abominação(o atirador escolhe,3- Corredor, 4- Necromnate.")
                print("O erro em magia ou arma de alcance gera FOGO AMIGO que estiver na zona, pode fazer rolagem de armadura, e distribuição livre dos danos.")
                print("Armas de alcance precisam ser carregadas após atirar")
                print("Gasta uma ação para recarregar, se transferir para outro apos tiro, precisa recarregar, a cada fase arma carrega automaticamente")
                print("Armas duplas gasta uma Ação para recarregar as duas, pode haver um tiro por ação nas armas duplas")
                print("Magia mesmas regras ditas acima")
                print("Fogo de dragão: bilis de dragão(ação descarte) + tocha(tocha depois, TODOS na zona morrem.")
                
            
            elif opcao_jogador == "6":
                print("\nPegar ou ativar um objeto")

            elif opcao_jogador == "7":
                print("\nFazer barulho")
                print("Coloque ficha de barulho no personagem")

            elif opcao_jogador == "8":
                print("\nNão fazer nada.")
    
            elif opcao_jogador == "9":
                continue
            else:
                print("\nEscolha inválida. Tente novamente.")
        
        elif escolha == "2":
            print("\nFase dos Zumbis:")
            print("1. Entrada de Zumbi")
            print("2. Mover ou Atacar")
            print("3. Corredores")
            print("4. Necromante")
            print("5. Tipos de Zumbis")
            print("6. Voltar")
            opcao_zumbi = input("\nEscolha uma ação (1-6): ")

            if opcao_zumbi == "1":
                print("\nEntrada de Zumbi:")
                print("Compre uma carta de zumbi para cada Zona de Entrada em sentido horário.")
                print("Zona de entrada colorida não entra zumbi ao menos que esteja na missão descrito.")
                print("\nCarta Ativação Extra - Uma ação extra para os zumbis indicados.")
                print("Carta Entrada Dupla - Nenhum zumbi aparece na zona designada, mas na próxima compra 2.")
                print("Se cair de novo, faça a entrada normal primeiro.")
                print("2x Cartas Duplas - 4 cartas na próxima zona.")
                print("Se não tiver zona ou for a última zona do tabuleiro, usar a dupla na primeira entrada ou zona de construção.")
            elif opcao_zumbi == "2":
                print("\nMover ou Atacar:")
                print("Necromante tem ação extra após todos os outros zumbis.")
                print("1. Ataque:")
                print("   1.1. Você está sendo atacado por um zumbi (1), abominação (2) ou fogo do dragão (3)?")
                print("        O ataque do zumbi causa 1 de dano, mas pode ser evitado com proteção. Tem proteção?")
                print("        Quer usar armadura ou escudo? Se optar pelo escudo, não pode rerolar.")
                print("            - Armadura equipada: Role o dado para cada dano >= Armadura evita ataque.")
                print("            - Escudo equipado: Permite rolar para armadura se não tiver armadura. Se tiver armadura, pode rerolar uma vez as rolagens de armadura.")
                print("   1.2. Abominação não te protege.")
                print("   1.3. Fogo do dragão não te protege.")
                print("\nMovimentação:")
                print("1. Prioridade: Se move para onde tem sobrevivente no campo de visão e mais barulho.")
                print("2. Movem-se em direção à rota mais curta. Se houver duas rotas, devem se dividir.")
                print("3. Se não houver rotas, vão para a porta.")
            elif opcao_zumbi == "3":
                print("\nCorredores:")
                print("Fazem uma ação extra após todos os zumbis. Pode ser ataque ou movimento.")
                print("1 de dano para morrer.")
            elif opcao_zumbi == "4":
                print("\nNecromante:")
                print("Coloque uma ficha de entrada de zumbi na zona do necromante.")
                print("Coloque o necromante nessa zona e compre uma nova carta de zumbi para essa zona imediatamente.")
                print("Isso transforma a zona em uma nova zona de entrada de zumbis.")
                print("O necromante foge pela zona de entrada mais próxima dele e ataca.")
                print("Se houver 6 zonas de entrada ativas, GAME OVER.")
                print("Se fugir, vira uma zona permanente e substitua a ficha por uma vermelha.")
                print("Se matar o necromante, remova uma ficha de entrada (inclusive a dele). Se não for a dele, substitua por uma vermelha.")
                print("OBS: Se todas as fichas de entrada ficarem no mesmo local, o necromante foge assim que ativado.")
            elif opcao_zumbi == "5":
                print("\nTipos de Zumbis:")
                print("Balofos: 2 de dano para morrer, não importa quantos hits.")
                print("Lerdos: 1 de dano para morrer.")
                print("Abominações: 3 de dano para morrer. Fogo de dragão ou Samson + corpo a corpo (dano 2 + habilidade 1) matam.")
            elif opcao_zumbi == "6":
                continue
            else:
                print("\nEscolha inválida. Tente novamente.")
        
        elif escolha == "3":
            print("\nSaindo do jogo. Até mais!")
            break
        
        else:
            print("\nEscolha inválida. Tente novamente.")

if __name__ == "__main__":
    zombicide_jogo()
