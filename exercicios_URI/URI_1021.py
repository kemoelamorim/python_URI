""" Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).

Saída
Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.

Obs: Utilize ponto (.) para separar a parte decimal.

"""
valor = float(input())
cedulas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print("NOTAS:")
for cedula in cedulas:
    fatoracao = int(valor/cedula)
    print(f"{int(fatoracao)} nota(s) de R$ {cedula:.2f}")    
    valor = valor % cedula
fracao = valor

print("MOEDAS:")
for moeda in moedas:
    decomposicao = int(round(fracao,2)/moeda)
    print(f"{int(decomposicao)} moeda(s) de R$ {moeda:.2f}")    
    fracao = fracao % moeda
