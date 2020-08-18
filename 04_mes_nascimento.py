'''

crie uma tupla para guardar os meses do ano.
Em seguida peça ao usuário a sua data de nascimento no formato
DD-MM-AAAA e guarde na varíavel data_nasc.
Ao final imprima "Você nasceu no mês de ______________", utilizando
o nome do mês da tupla corresponddente ao mês informado pelo usuário.

Dica: você vai precisar fazer slicing na data de nascimento informada 
para ter o Mês. Depois você terá que buscar o mês na tupla através do índice

'''


import math

print("\n|--------------Imprimindo mês do nascimento---------------|\n\n")

meses_ano = ('janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro')

data_nasc = input('Insira a sua data de nascimento no formato DD-MM-AAAA: ')

indice = int(data_nasc[3:5]) - 1

mes_nasc = meses_ano[indice]


print("\n\n|---------------------------------------------------------|\n")

print("|-------------- Você nasceu no mês de",mes_nasc,"---------------|");

print("\n|--------------------Fim do programa----------------------|\n")

input('Pressione enter para finalizar o programa.\n')