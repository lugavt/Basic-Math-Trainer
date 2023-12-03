import numpy as np
from time import time


def operacao(nivel):
    if nivel == 1:
        return np.random.randint(0, 2)
    return np.random.randint(0, 4)

def trunc(num, digits):
   sp = str(num).split('.')
   return int('.'.join([sp[0], sp[:digits]]))

print("Bem-vindo ao treino de contas de matemática!")
print("Escolha o nível de dificuldade:")
print("1 - Fácil")
print("2 - Normal")

operacoes = ("+", "-", "*", "/")
nivel = int(input("Nível: "))
print("Legal! Quanto tempo você quer treinar? (em minutos)")
tempo = int(input("Tempo: "))
tempo = tempo * 60
tempolimite = time() + tempo
conta = 0
acertos = 0
erros = 0
print("Beleza! Vamos lá")
while(time() < tempolimite):
    conta += 1
    print("\nConta número: ", conta)
    op = operacao(nivel)
    a = np.random.randint(0, 1000)
    b = np.random.randint(0, 1000)
    print(a, operacoes[op], b)
    resposta = int(input("Resposta: "))
    esperado = eval(str(a)+operacoes[op]+str(b))
    if operacoes[op] == "/":
        esperado = trunc(esperado, 2)
    if resposta == esperado:
        print("Acertou!")
        acertos += 1
    else:
        while(resposta != eval(str(a)+operacoes[op]+str(b))):
            print("Errou! Tente novamente")
            erros += 1
            resposta = int(input("Resposta: "))
        print("Acertou!")
print("acertos: ", acertos)
print("erros: ", erros) 