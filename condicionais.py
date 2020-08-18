'''

arquivo para aula de condicionais

'''

idade = int(input('Insira a sua idade: '))
sexo = input('Insira o sexo(M ou F): ').lower()
cidade = input('Insira sua cidade: ').lower()


if cidade == 'rio' or cidade == 'são paulo':
	if sexo == 'm':
		if idade >= 18:
			print('Sexo masculino, maior de idade e morador da região sudeste!')
		else:
			print('Sexo masculino, menor de idade e morador da região sudeste!')
	elif sexo == 'f':
		if idade >= 18:
			print('Sexo feminino, maior de idade e moradora da região sudeste!')
		else:
			print('Sexo feminino, menor de idade e moradora da região sudeste!')
	else:
		print('Erro na entrada de dados!!')
else:
	print('Entrada de dados incorreta ou cidade não pertence a região sudeste!')
