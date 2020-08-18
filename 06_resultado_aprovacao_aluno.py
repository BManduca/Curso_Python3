'''

Peça ao usuario as seguintes informações sobre um aluno:

Nome
Nota prova 1
Nota prova 2
Total de faltas

Considere que foram dadas 20 aulas e que para passar o aluno precisa de pelo
menos 70% de presença e média 6,0 ou mais.
Ao final imprima
 -> Nome do Aluno
 -> Média
 -> Percentual de Presença(assiduidade)
 -> Resultado(Repovado por falta e média, Reprovado por Faltas, Reprovado por média,
 Aprovado)


Novo Exercicio:

no programa que calcula a média e imprime a situação do aluno, foi feito
no exercicio sobre condicionais. Aplique a validação de dados para que:

-> o programa nunca seja interrompido por erro
-> a nota seja entre 0 e 10
-> o peso seja entre 0 e 10
-> o número de faltas seja entre 0 e 20


'''

print("\n|----------------------Boletim anual-----------------------|\n\n")

def ponderada(peso1,peso2,prova1,prova2):

	soma_pesos = peso1 + peso2;

	med = ((peso1 * prova1) + (peso2 * prova2)) / soma_pesos;

	return med;



nome = input('Insira o nome do Aluno: ');

controle_boletim = False;

while controle_boletim == False:
	nota1 = input('Insira a nota da prova 1: ');
	try:
		nota1 = float(nota1);
		if nota1 < 0 or nota1 > 10:
			print('Nota 1 inserida está incorreta! O valor precisa estar entre 0 e 10!');
		else:
			controle_boletim = True;
	except:
		print('Valor da nota é inválido! Favor utilizar somente números e separar os decimais através do ".".  (Ex.: 9.5)');


controle_boletim = False;

while controle_boletim == False:
	nota2 = input('Insira a nota da prova 2: ');
	try:
		nota2 = float(nota2);
		if nota2 < 0 or nota2 > 10:
			print('Nota 2 inserida está incorreta! O valor precisa estar entre 0 e 10!');
		else:
			controle_boletim = True;
	except:
		print('Valor da nota é inválido! Favor utilizar somente números e separar os decimais através do ".".  (Ex.: 9.5)');


controle_boletim = False;

while controle_boletim == False:
	peso1 = input('Insira peso da prova 1: ');
	try:
		peso1 = float(peso1);
		if peso1 < 0 or peso1 > 10:
			print('Peso 1 está incorreto! O valor precisa estar entre 0 e 10!');
		else:
			controle_boletim = True;
	except:
		print('Valor do peso é inválido! Favor utilizar somente números e separar os decimais através do ".".  (Ex.: 3.5)');



controle_boletim = False;

while controle_boletim == False:
	peso2 = input('Insira peso da prova 2: ');
	try:
		peso2 = float(peso2);
		if peso2 < 0 or peso2 > 10:
			print('Peso 2 está incorreto! O valor precisa estar entre 0 e 10!');
		else:
			controle_boletim = True;
	except:
		print('Valor do peso é inválido! Favor utilizar somente números e separar os decimais através do ".".  (Ex.: 3.5)');


controle_boletim = False;	

while controle_boletim == False:
	total_faltas = input('Insira o total de faltas do aluno: ');
	try:
		total_faltas = float(total_faltas);
		if total_faltas < 0 or total_faltas > 20:
			print('Total de faltas está incorreto! O valor precisa estar entre 0 e 20!');
		else:
			controle_boletim = True;
	except:
		print('Quantidade de faltas está inválido! Favor utilizar somente números e separar os decimais através do ".".  (Ex.: 15.5)');	
	

media = ponderada(peso1,peso2,nota1,nota2);
presenca = (20 - total_faltas);
assiduidade = ((100 * presenca) / 20);


if assiduidade >= 70 and media >= 6.0:
	mensagem = 'Aluno aprovado com mérito!';
elif assiduidade >= 70 and media < 6.0:
	mensagem = 'Aluno reprovado por média!!';
elif assiduidade < 70 and media >= 6.0:
	mensagem = 'Aluno reprovado por faltas!!';
else:
	mensagem = 'Aluno reprovado por falta e média!!';

print("\n\n|---------------------------------------------------------|\n");

print('Aluno:',nome,'\n');
print('Média:',f'{media:.2f}\n');
print('Percentual de presença(assiduidade):',str(assiduidade) + '%\n');
print('Resultado:',mensagem);

print("\n|--------------------Fim do programa----------------------|\n");

input('Pressione enter para finalizar o programa.\n');