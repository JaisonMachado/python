#jogo da velha
#exercicio de aula Python - Cisco Networking Academy
#21 de outubro de 2021
# Jaison Machado
#tabuleiro

import random
def tabuleiro():
    print(l1[0],l1[1],l1[2])
    print(l2[0],l2[1],l2[2],l2[3],l2[4],l2[5],l2[6])
    print(l1[0],l1[1],l1[2])
    print(l3[0],l3[1],l3[2],l3[3],l3[4],l3[5],l3[6])
    print(l1[0],l1[1],l1[2])
    print(l4[0],l4[1],l4[2],l4[3],l4[4],l4[5],l4[6])
    print(l1[0],l1[1],l1[2])
def inicia():
    print("Computador escolheu!")
    l3[3]="X"
def pc_joga():
    livre=[]
    livre=casa_livre()
    escolha=int(random.choice(livre))
    print(escolha)
    if escolha==1:
        l2[1]="X"
    elif escolha==2:
        l2[3]="X"
    elif escolha==3:
        l2[5]="X"
    elif escolha==4:
        l3[1]="X"
    elif escolha==6:
        l3[5]="X"
    elif escolha==7:
        l4[1]="X"
    elif escolha==8:
        l4[3]="X"
    elif escolha==9:
        l4[5]="X"
def casa_livre():
    livre=[]
    copia=[l2[1],l2[3],l2[5],l3[1],l3[3],l3[5],l4[1],l4[3],l4[5]]
    for i in range(0,len(copia)):
        if copia[i]=="X" or copia[i]=="O":
            continue
        livre.append(copia[i])
    if len(livre)>=1: 
        return livre
    else:
        return None
    
def sua_vez():
    escolha=int(input("escolha entre as casas livres:"))
    global controle
    if escolha == 0:
        controle=escolha
        return
    if escolha==1:
        l2[1]="O"
    elif escolha==2:
        l2[3]="O"
    elif escolha==3:
        l2[5]="O"
    elif escolha==4:
        l3[1]="O"
    elif escolha==6:
        l3[5]="O"
    elif escolha==7:
        l4[1]="O"
    elif escolha==8:
        l4[3]="O"
    elif escolha==9:
        l4[5]="O"
    
    return controle
def ganhador():
    #vitoria na linha 2
    if (l2[1]==l2[3]) and (l2[3]==l2[5]):
        return 1
    #vitoria na linha 3
    elif (l3[1]==l3[3]) and (l3[3]==l2[5]):
        return 1
    #vitoria na linha 4
    elif (l4[1]==l4[3]) and (l4[3]==l4[5]):
        return 1
    #vitoria na diagonal 1-3-5 
    elif (l2[1]==l3[3]) and (l3[3]==l4[5]):
        return 1
    #vitoria na diagonal 3-5-7 
    elif (l2[5]==l3[3]) and (l3[3]==l4[1]):
        return 1
    #vitoria na vertical central 2-5-8
    elif (l2[3]==l3[3]) and (l3[3]==l4[3]):
        return 1
    #vitoria na vertical 1-4-7
    elif (l2[1]==l3[1]) and (l3[1]==l4[1]):
        return 1
    #vitoria na vertical 3-6-9
    elif (l2[5]==l3[5]) and (l3[5]==l4[5]):
        return 1
    else:
        return 0
controle=1
l1=["+=====","======","======+"]
l2=["| ",1," |  ",2," | ",3,"  |"]
l3=["| ",4," |  ","X"," | ",6,"  |"]
l4=["| ",7," |  ",8," | ",9,"  |"]
tabuleiro()
print("Casas disponíveis:",casa_livre())
sua_vez()
while(controle!=0):
    tabuleiro()
    if (casa_livre() == None):
        print("Fim de jogo!")
        break
    pc_joga()
    tabuleiro()
    if (casa_livre() == None):
        print("Fim de jogo!")
        break
    if (ganhador()==1):
       print("Fim de jogo, PC ganhou!")
       break
    print("Casas disponíveis:",casa_livre())
    sua_vez()
    if (ganhador()==1):
        tabuleiro()
        print("Fim de jogo, você ganhou!")
        break
