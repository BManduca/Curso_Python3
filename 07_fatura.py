'''

Faça um programa para registrar uma venda. O programa vai receber do usuario
o nome do produto e o preço e vai adiciona-lo à fatura. Em seguida, 
pergunte ao usuário se ele quer comprar mais algum produto.

se a resposta for 'sim', repita a opreção. Só pare quando a resposta
form 'não' e então imprima a fatura, que deve conter os produtos
comprados e os preços. Ao final deve apresentar o total da fatura.

obs.: para facilitar a reslução do exercicio, considere que só e possível
comprar uma unidade de cada produto de cada vez.

'''

print("\n|--------------------------Iniciando fatura---------------------------|\n\n")


controle = 'sim'
lista_fatura = []
total = 0
total_quant_preco = 0
validar_preco = False


while controle == 'sim':
	produto = input('Insira o nome do produto: ');

	'''
		para validar a entrada de dados do preço,
		faremos uma entrada normal(input) e após, 
		faremos um loop, para que verifique a mesma
		entrada e somente saira do loop, se 
		conseguir validar que a mesma foi inserida
		como esperado.
	'''

	while validar_preco == False:
		preco = input('Insira o preço do produto: ');
		try:
			preco = float(preco)
			if preco <= 0:
				print('O preço inserido precisa ser maior que zero!\n')
			else:
				##se caso o programa conseguir converter, a variável recebe True e sai da validação, senão, continuara dentro do while
				validar_preco = True
		except:
			print('Formato de preço inserido está inválido!')
			print('Insira somente números e ao separar os centavos, utilizar o "."!\n')
		# else:
		# 	pass
		# finally:
		# 	pass

	quant = int(input('Insira a quantidade comprada: '));
	total_quant_preco = (preco * quant);
	lista_fatura.append([produto,quant,preco,total_quant_preco]);
	total += total_quant_preco;
	validar_preco = False
	controle = input('Gostaria de efetuar a compra de mais algum item? (SIM ou NAO): ').lower();
	print('\n')

print("\n\n|---------------------------Gerando Nota------------------------------|\n")

for x in lista_fatura:
	print(' Produto: ' + str(x[0]) + '\n Quantidade: ' + str(x[1]) + '\n Preço: ' + str(x[2]) + '\n Valor total do produto => R$' + str(x[3]) + '\n');


print('\n Total da fatura da compra:',f'{total:.2f}','reais')
print("\n|----------------------------Fim da fatura------------------------------|\n")

input('Pressione enter para finalizar o programa.\n')