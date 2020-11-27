""" A tarefa aqui neste problema é ler uma expressão matemática na forma de dois números Racionais (numerador / denominador) e apresentar o resultado da operação. Cada operando ou operador é separado por um espaço em branco. A sequência de cada linha que contém a expressão a ser lida é: número, caractere, número, caractere, número, caractere, número. A resposta deverá ser apresentada e posteriormente simplificada. Deverá então ser apresentado o sinal de igualdade e em seguida a resposta simplificada. No caso de não ser possível uma simplificação, deve ser apresentada a mesma resposta após o sinal de igualdade.

Considerando N1 e D1 como numerador e denominador da primeira fração, segue a orientação de como deverá ser realizada cada uma das operações:
Soma: (N1*D2 + N2*D1) / (D1*D2)
Subtração: (N1*D2 - N2*D1) / (D1*D2)
Multiplicação: (N1*N2) / (D1*D2)
Divisão: (N1/D1) / (N2/D2), ou seja (N1*D2)/(N2*D1)

Entrada:
A entrada contem vários casos de teste. A primeira linha de cada caso de teste contem um inteiro N (1 ≤ N ≤ 1*104), indicando a quantidade de casos de teste que devem ser lidos logo a seguir. Cada caso de teste contém um valor racional X (1 ≤ X ≤ 1000), uma operação (-, +, * ou /) e outro valor racional Y (1 ≤ Y ≤ 1000).

Saída:
A saída consiste em um valor racional, seguido de um sinal de igualdade e outro valor racional, que é a simplificação do primeiro valor. No caso do primeiro valor não poder ser simplificado, o mesmo deve ser repetido após o sinal de igualdade. 
"""

casosdeTeste = int(input())
for caso in range(0,casosdeTeste):
    n1, div1, d1, operador, n2, div2, d2 = input().split(' ')
    n1 = int(n1)
    n2 = int(n2)
    d1 = int(d1)
    d2 = int(d2)

def mdc(n1, n2):
    resto = None
    while resto != 0:
        resto = n1 % n2
        n1 = n2
        n2 = resto
    return n1

def soma():
    numerador = (n1*d2 + n2*d1)
    denominador = (d1*d2)
    simplificacaoNum = numerador / int(mdc(numerador, denominador))
    simplificacaoDen = denominador / mdc(n1, n2)
    return print(f'{numerador}/{denominador} = {int(simplificacaoNum)}/{int(simplificacaoDen)}')

def subtracao():
    numerador = (n1*d2 - n2*d1)  
    denominador = (d1*d2)
    simplificacaoNum = numerador / int(mdc(numerador, denominador))
    simplificacaoDen = denominador / mdc(n1, n2)
    return print(f'{numerador}/{denominador} = {int(simplificacaoNum)}/{int(simplificacaoDen)}')

def multiplicacao():
    numerador = (n1*n2) 
    denominador = (d1*d2)
    simplificacaoNum = numerador / int(mdc(numerador, denominador))
    simplificacaoDen = denominador / mdc(n1, n2)
    return print(f'{numerador}/{denominador} = {int(simplificacaoNum)}/{int(simplificacaoDen)}')
def divisao():
    numerador = (n1/d1) 
    denominador = (n2/d2)
    simplificacaoNum = int(numerador) / int(mdc(numerador, denominador))
    simplificacaoDen = denominador / mdc(n1, n2)
    return print(f'{numerador}/{denominador} = {int(simplificacaoNum)}/{int(simplificacaoDen)}')

if operador == '+':
    soma()
elif operador == '-':
    subtracao()
elif operador == '*':
    multiplicacao()
elif operador == '/':
    divisao()
    
# corrigir erros no calculo da divisão  