'''

Faça um programa para calcular a média podnerada de um aluno. Para isso, peça ao usuario
os pesos das duas provas e as notas do aluno. Ao final, imprima a média ponderada do aluno

'''

import math

print("\n|----------Imprimindo a média ponderada de um aluno-----------|\n")

def ponderada(peso1,peso2,prova1,prova2):

	soma_pesos = peso1 + peso2

	med = ((peso1 * prova1) + (peso2 * prova2)) / soma_pesos

	return med

peso1 = float(input('Insira o peso da primeira prova: '))
peso2 = float(input('Insira o peso da segunda prova: '))
prova1 = float(input('Insira a nota da prova 1: '))
prova2 = float(input('Insira a nota da prova 2: '))

print("\n|---------------------------------------------------------|\n")

med_pond = ponderada(peso1,peso2,prova1,prova2)

print(' | Nota da primeira prova:',prova1,"|\n | Peso da primeira prova:",peso1,"|")
print('\n | Nota da segunda prova:',prova2,"|\n | Peso da segunda prova:",peso2,"|")
print("\n | Resultado da média ponderada do Aluno é:",med_pond,"|")

print("\n|--------------------Fim do programa----------------------|\n")

input('Pressione enter para finalizar o programa.\n')