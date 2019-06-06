import time
from random import randint

agente = "#"
limpo = 0
ambiente = [[1,4,0,0,2,0,3],
            [0,0,3,1,0,4,0],
            [0,1,0,0,2,0,0],
            [0,0,2,1,0,1,2],
            [2,0,3,0,3,1,4],
            [0,4,0,0,3,1,4],
            [0,1,1,0,2,3,0]]
        
def printar(ambiente):
    for secao in ambiente:
        print(secao)
    print(30*"\n")

def sujaambiente(ambiente):
    for secao in ambiente:
        atual = 0
        for local in secao:
            secao[atual] = randint(0,4)
            atual +=1
    return ambiente

printar(ambiente)
#limpar tela
time.sleep(0.5)

def aspirador(ambiente):
    for secao in ambiente:
        atual = 0
        for local in secao:
            if local != limpo:
                secao[atual] = agente

                printar(ambiente)
                time.sleep(0.5)

                secao[atual] = limpo
                atual +=1
            else:
                    salva = secao[atual]
                    secao[atual] = agente
                    printar(ambiente)
                    secao[atual] = salva
                    time.sleep(0.5)

                    atual +=1
                    continue
    return ambiente

while True:
    printar(aspirador(ambiente))
    ambiente = sujaambiente(ambiente)
    printar(ambiente)
    time.sleep(1)

    


