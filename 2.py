"""
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a 
soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um 
programa na linguagem que desejar onde, informado um número, ele calcule a sequência de 
Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
"""

while True:
    n = int(input('Digite um número: '))
    if n > 0:
        break
    print('Número inválido! Tente novamente')

ant = 0
prox = 0
condicao = False

print("Sequencia de fibonnaci:")
while prox <= n:
    if (prox == n):
        condicao = True
    print(prox)
    prox = prox + ant
    ant = prox - ant
    if prox == 0:
        prox = prox + 1

print('\n')
print(f'{n} está na sequência' if condicao else f'{n} não está na sequência')
