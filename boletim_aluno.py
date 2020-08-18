'''

arquivo para aula de condicionais

'''

# idade = int(input('Insira sua idade: '))

# if idade >= 18:
# 	print(' Maior de idade! Entrada liberada.')
# else:
# 	print(' Menor de idade! Entrada Proíbida.') 

print("\n|------------------Boletim de Aluno-------------------|\n")

nota = float(input('Insira a nota da prova: '))

if nota >= 7.0:
	print("\n |---------------------------------------|")
	print("   Aluno aprovado! Boas férias!")
	print(" |---------------------------------------|\n")
elif (nota < 7.0) and (nota >= 3.0):
	print("\n |--------------------------------------------|")
	print("   Aluno de recuperação!\n")
	recuperacao = float(input('   Insira a nota da prova de recuperacao: '))

	if recuperacao >= 6.0:
		print("\n   Aluno aprovado! Boas férias")
	else:
		print("\n   Aluno reprovado!")
	print(" |--------------------------------------------|\n")
else:
	print("\n |--------------------------------------------|")
	print("   Aluno reprovado!")
	print(" |--------------------------------------------|\n")

print("\n|-----------------------------------------------------|\n\n")