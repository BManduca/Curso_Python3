'''
#aula 15 - Loops: While
x = 0

pessoas = []

print('|------------------------------------|')
while ('joão' and 'joao') not in pessoas:
	nome = input('\n Insira um nome: ')
	#print('\n Nome(' + str(x) + '):',nome)
	if nome == 'joão' or nome == 'joao':
		#continue
		break

	pessoas.append(nome)
	x += 1

print('\n|--------------------------Ordenando a Lista--------------------------|')
pessoas_ordenado = sorted(pessoas)
print('\n Listagem ordenada:',pessoas_ordenado,'\n')
print('|---------------------------------------------------------------------|\n\n')

'''


'''
#Aula 16 - Loopś: For
#loop for com listas e strings

compras  = ['arroz','feijão','carne','temperos']

nome = 'Brunno'


for i in compras:
	#funcao index serve para retornar a posicao dentro da lista
	print('compras(' + str(compras.index(i)) + '):',i)	


for x in nome:
	print('nome(' + str(nome.index(x)) + '):',x)

'''

'''

#somatorio com for loop

vendas = [1000,450,900,600,300,700,980,432,1100]
total = 0

print('|-----------------------------------------------------------|\n')
for x in vendas:
	print(' vendas(' + str(vendas.index(x)) + '):',x,'reais')
	total += x

print('\n Total da venda:',total,'reais\n')
print('|-----------------------------------------------------------|\n\n')

'''

'''

#dicionario com for loop



cores = {'verde': 'green','azul': 'blue','rosa': 'pink','vermelho': 'red','branco': 'white','preto': 'black'}


print('|-----------------------------------------------------------|\n')
for x in cores:
	print(' cores(' + x + '):',cores[x])
	
#print('\n Total da venda:',total,'reais\n')
print('\n|-----------------------------------------------------------|\n\n')

'''


'''

#for loop aninhado


compras  = [['arroz','feijão','temperos'],['carne','frango','peixe'],['leite','iogurte','ovos'],['maçã','banana','mamão']]


for x in compras:
	print('|-----------------------------------------------------------|')
	print('\n lista de compras ' + str(compras.index(x)) + ':')
	for y in x:
		print('\n Item ' + str(x.index(y)) + ':', y)
	print('\n|-----------------------------------------------------------|\n\n')
print('\n Fim da lista de compras!')

'''

pessoas = []

for x in range(1,10):
	nome = input('\n Insira um nome: ')
	pessoas.append(nome)

print('\n|--------------------------Ordenando a Lista--------------------------|')
pessoas_ordenado = sorted(pessoas)
print('\n Listagem ordenada:',pessoas_ordenado,'\n')
print('|---------------------------------------------------------------------|\n\n')