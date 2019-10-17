import random

#def croupier(croupier):
#    for i in range(0,2):
#        croupier.append(baralho[i])
#    if soma_C(croupier) < 18:
#        for i in range(4,6):
#            croupier.append(baralho[i])
    

def soma_C(croupier):
    soma_C=0
    i=0
    
    while i <len(croupier):
        if croupier[i]=='2':
            soma_C+=2
        if croupier[i]=='3':
            soma_C+=3
        if croupier[i]=='4':
            soma_C+=4
        if croupier[i]=='5':
            soma_C+=5
        if croupier[i]=='6':
            soma_C+=6
        if croupier[i]=='7':
            soma_C+=7
        if croupier[i]=='8':
            soma_C+=8
        if croupier[i]=='9':
            soma_C+=9
        if croupier[i]=='10':
            soma_C+=10
        if croupier[i]=='J':
            soma_C+=10
        if croupier[i]=='Q':
            soma_C+=10
        if croupier[i]=='K':
            soma_C+=10
        if croupier[i]=='A':
            soma_C+=11
            if soma_C > 21:
                soma_C-=10
        i+=1
    return(soma_C)

def soma_J(jogador):
    soma_J=0
    i=0
    
    while i <len(jogador):
        if jogador[i]=='2':
            soma_J+=2
        if jogador[i]=='3':
            soma_J+=3
        if jogador[i]=='4':
            soma_J+=4
        if jogador[i]=='5':
            soma_J+=5
        if jogador[i]=='6':
            soma_J+=6
        if jogador[i]=='7':
            soma_J+=7
        if jogador[i]=='8':
            soma_J+=8
        if jogador[i]=='9':
            soma_J+=9
        if jogador[i]=='10':
            soma_J+=10
        if jogador[i]=='J':
            soma_J+=10
        if jogador[i]=='Q':
            soma_J+=10
        if jogador[i]=='K':
            soma_J+=10
        if jogador[i]=='A':
            soma_J+=11
            if soma_J > 21:
                soma_J-=10
        i+=1
    return(soma_J)
    
def joker(jogador):
    joker=0
    for i in len(jogador):
        if jogador[i]=='JOKER':
            joker+=100
            return joker
    
creditos = 100

nome=input("Digite seu nome: ")

print("")
print("------------------------------------------------------------")
print("Olá, {0}!".format(nome))
print("")
print("Bem-vindo ao BlackJack em Python, você irá começar com {0} créditos e através de apostas você poderá ganhar mais créditos ou perder todos eles.".format(creditos))
print("Boa Sorte!")
print("")

print("------------------------------------")
print("Primeiro escolha o seu modo de jogo:")
print("------------------------------------")
print("- Solo")
print("- Multijogador")

modo_de_jogo=input("Qual o modo de Jogo? ")
print("")
while modo_de_jogo != 'Solo' and modo_de_jogo != 'solo' and modo_de_jogo != 'S' and modo_de_jogo != 's' and modo_de_jogo != 'Multijogador' and modo_de_jogo != 'multijogador' and modo_de_jogo != 'M' and modo_de_jogo != 'm':
    print("Inválido!")
    modo_de_jogo=input("Qual o modo de Jogo? ")
    print("")

print("----------------------------------------------------------")
print("Agora insira a quantidade de baralhos que você gostaria de jogar: ")
print("----------------------------------------------------------")
print("- Apenas 1")
print("- 2 ou + (digite a quantidade)")
quant_baralhos=int(input("Quantidade de baralhos: "))
print("")

if modo_de_jogo == 'Solo' or modo_de_jogo == 'solo' or modo_de_jogo == 'S' or modo_de_jogo == 's':
    
    croupier = []
    jogador = []
    
    while creditos > 0:
        print("")
        print("----------------")
        print("Valor da Aposta:")
        print("----------------")
        print("- Você possui {0} créditos restantes.".format(creditos))
        
        aposta=int(input("Qual o valor da sua aposta? "))
        if aposta == 'Fim' or aposta == 'fim':
            break
        
        if aposta > creditos:
            while aposta > creditos:
                print("")
                print("Você não possui todos esses créditos")
                aposta=int(input("Qual o valor da sua aposta? "))

        creditos-=aposta
        
        baralho = quant_baralhos * 4*['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        baralho.append('JOKER')
        random.shuffle(baralho)
        
        print("")
        print("----------------------------------------------------------")
        print("As Cartas do Croupier são:")
        print("----------------------------------------------------------")
        for i in range(1):
            croupier.append(baralho[i])
        print(croupier)
        
        print("")    
        print("----------------------------------------------------------")
        print("As cartas de {0} são:".format(nome))
        print("----------------------------------------------------------")
        for i in range(2,4):
            jogador.append(baralho[i])
        print(jogador)
        
        if soma_J(jogador) == 21:
            print("")
            print("")
            print("")
            print("")
            print("")
            print("----------------------------------------------------------")
            print("As Cartas do Croupier são:")
            print("----------------------------------------------------------")
            
            croupier=[]
            for i in range(0,2):
                croupier.append(baralho[i])
            print(croupier)
        
            print("")    
            print("----------------------------------------------------------")
            print("As cartas de {0} são:".format(nome))
            print("----------------------------------------------------------")
            jogador=[]
            for i in range(2,4):
                jogador.append(baralho[i])
            print(jogador,' Um BlackJack!!')
            
            if soma_C(croupier) != 21:
                print("")
                print("Parabéns um BlackJack!")
                print("Você ganhou {0} créditos.".format(1.5*aposta))
                creditos+=aposta+1.5*aposta
            
            if soma_C(croupier) == 21:
                print("")
                print("Como o croupier também conseguiu um BlackJack,")
                print("você não ganhou nem perdeu nada.")
                print("Você ganhou 0 créditos.")
             
        else:
            jogo = True
            while jogo:
                print("-----------------------------------")
                print("Agora você tem uma decisão a fazer:")
                print("-----------------------------------")
                print("- Mais cartas")
                print("- Sair")
                
                escolha=input("Qual a sua decisão? ")
                while escolha != 'Mais cartas' and escolha != 'mais cartas' and escolha != 'Mais' and escolha != 'mais' and escolha != 'Sair' and escolha != 'sair' and escolha != 'Split' and escolha != 'split':
                    print("Inválido!")
                    escolha=input("Qual a sua decisão? ")
                    
                if escolha == 'Sair' or escolha == 'sair':
                    print("Você escolheu sair.")
                    
                    print("----------------------------------------------------------")
                    print("As Cartas do Croupier são:")
                    print("----------------------------------------------------------")
                    croupier=[]
                    
                    for i in range(0,2):
                        croupier.append(baralho[i])
                    print(croupier)
                    
                    print("")    
                    print("----------------------------------------------------------")
                    print("As cartas de {0} são:".format(nome))
                    print("----------------------------------------------------------")
                    jogador=[]
                    for i in range(2,4):
                        jogador.append(baralho[i])
                    print(jogador)
                    
                if escolha == 'Mais cartas' or escolha == 'mais cartas' or escolha == 'Mais' or escolha == 'mais':
                    
                    while soma_J(jogador) <= 21 or escolha == 'Sair' or escolha == 'sair':
                    
                        print("----------------------------------------------------------")
                        print("As Cartas do Croupier são:")
                        print("----------------------------------------------------------")
                        croupier=[]
                        for i in range(0,2):
                            croupier.append(baralho[i])
                            
                        if soma_C(croupier) < 18:
                            croupier.append(baralho[i])
                        print(croupier)
                        
                        print("")    
                        print("----------------------------------------------------------")
                        print("As cartas de {0} são:".format(nome))
                        print("----------------------------------------------------------")
                        jogador=[]
                        
                        i=4
                        jogador.append(baralho[i])
                        i+=1
                        print(jogador)
                        
                        if soma_J(jogador) > 21:
                            print("Você perdeu porque estorou!")
                            print("Você perdeu {0} créditos".format(aposta))
                        
                    print("----------------------------------------------------------")
                    print("As Cartas do Croupier são:")
                    print("----------------------------------------------------------")
                    croupier=[]
                    for i in range(0,2):
                        croupier.append(baralho[i])
                        
                    if soma_C(croupier) < 18:
                        croupier.append(baralho[i])
                    print(croupier)
                    
                    print("")    
                    print("----------------------------------------------------------")
                    print("As cartas de {0} são:".format(nome))
                    print("----------------------------------------------------------")
                    jogador=[]
                    
                    print(jogador)
        
                    
#if soma_J(jogador) > 21:
#    print("")
#    print("Você perdeu porque estourou suas cartas!")
#    print("Você perdeu {0} créditos.".format(aposta))
#    jogo = False
##    
#    if soma_J(jogador) > soma_C(jogador):
#        
#        print("")
#        print("As cartas do ")
#        
#        print("Parabéns, você venceu!")
#        print("Você ganhou {0} créditos.".format(aposta))
#        creditos+=aposta+aposta
#        jogo = False
#        
#    if soma_J(jogador) < soma_C(jogador):
#        print("Você perdeu")
#        print()
#
#if soma_J(jogador) < 21:
                
    

            
   













     

if modo_de_jogo == 'Multijogador' or modo_de_jogo == 'multijogador' or modo_de_jogo == 'M' or modo_de_jogo == 'm':
    print("oi")


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

print("")
print("-----------------------------------------")
print("FIM DE JOGO")
print("Obrigado por jogar!")
print("Feito por Gabriel Yamashita e Laura Perim")
print("-----------------------------------------")