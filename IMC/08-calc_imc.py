'''

Programa para calcular o IMC e devolver mensagem de classificação e efeitos
com relação ao mesmo.


print("\n|-----------------------------------Cálculo do IMC------------------------------------|\n\n")

def imc(peso,altura):
    res_imc = peso / (altura * altura);

    return res_imc;

nome = input('Insira o nome do Paciente: ');
peso_paciente = float(input('Insira o peso do paciente: '));
alt_paciente = float(input('Insira a altura do paciente: '));

calc_imc = imc(peso_paciente,alt_paciente);

if calc_imc >= 16 and calc_imc <= 16.9:
    resultado = 'Classificação: Muito abaixo do peso!  |  Efeitos: Queda de cabelo, infertilidade, ausência menstrual.';
elif calc_imc >= 17 and calc_imc <= 18.4:
    resultado = 'Classificação: Abaixo do peso!  |  Efeitos: Fadiga, stress, ansiedade.';
elif calc_imc >= 18.5 and calc_imc <= 24.9:
    resultado = 'Classificação: Peso normal!  |  Efeitos: Menor risco de doenças cardíacas e vasculares.';
elif calc_imc >= 25 and calc_imc <= 29.9:
    resultado = 'Classificação: Acima do peso!  |  Efeitos: Fadiga, má circulação, varizes.';
elif calc_imc >= 30 and calc_imc <= 34.9:
    resultado = 'Classificação: Obesidade Grau I!  |  Efeitos: Diabetes, angina, infarto, aterosclerose.';
elif calc_imc >= 35 and calc_imc <= 40:
    resultado = 'Classificação: Obesidade Grau II!  |  Efeitos: Apneia do sono, falta de ar.';
elif calc_imc > 40:
    resultado = 'Classificação: Obesidade Grau III!  |  Efeitos: Refluxo, dificuldade para se mover, escaras, diabetes, infarto, AVC.';

print("\n\n|-----------------------------------------------------------------------------------|\n");

print('Paciente:',nome,'\n');
print('Cálculo do IMC: ' + str(f'{calc_imc:.2f}') + ' kg/m2.\n');
print('Resultado:',resultado);

print("\n|----------------------------------Fim do programa------------------------------------|\n");

input('Pressione enter para finalizar o programa.\n')



'''



'''

Segundo exercicio:
Programa que receba o sexo, peso e a altura do usuário e em seguida apresente:
- IMC
- Classificação do IMC baseado na tabela

Condição                              M                        H

abaixo do peso                     < 19.1                   < 20.7
no peso normal                 > 19.1 e <= 25.8         > 20.7 e <= 26.4
marginalmente acima do peso    > 25.8 e <= 27.3         > 26.4 e <= 27.8
acima do peso ideal            > 27.3 e <= 32.3         > 27.8 e <= 31.1
obeso                              > 32.3                    > 31.1

'''

import func_calc_imc as fimc


print("\n|-----------------------------------Cálculo do IMC------------------------------------|\n\n")


nome = input(' Insira o nome do Paciente: ');
print('\n');

valid_sexo = False;

while valid_sexo == False:
	sexo = input(' Insira o sexo do Paciente (M ou F): ').lower();
	try:
		if sexo != 'f' and sexo != 'm':
			print('\n Sexo do paciente foi inserido incorretamente!\nFavor inserir F -> Feminino ou M -> Masculino!\n');
		else:
			valid_sexo = True;
			print('\n');
	except:
		print(' Valor inserido é inválido!\n Favor não inserir valores que diferem do que foi solicitado!');


valid_peso = False;

while valid_peso == False:
	peso_paciente = input(' Insira o peso do paciente: ');
	try:
		peso_paciente = float(peso_paciente);
		if peso_paciente < 0 or peso_paciente > 300:
			print(' Peso do Paciente inserido está incorreto! O valor precisa ser maior que 0');
		else:
			valid_peso = True;
			print('\n');
	except:
		print(' Valor do peso é inválido! Favor utilizar somente números e separar os decimais através do ".".  (Ex.: 39.5)');


valid_alt = False;

while valid_alt == False:
	alt_paciente = input(' Insira a altura do paciente: ');
	try:
		alt_paciente = float(alt_paciente);
		if alt_paciente < 0 or alt_paciente > 3:
			print(' Altura do Paciente inserido está incorreto! O valor precisa ser maior que 0');
		else:
			valid_alt = True;
			print('\n');
	except:
		print(' Valor da altura é inválido! Favor utilizar somente números e separar os decimais através do ".".  (Ex.: 1.75)');


v_imc = str(fimc.imc(peso_paciente,alt_paciente));
c_imc = fimc.class_imc(sexo,peso_paciente,alt_paciente);


print("|-----------------------------------------------------------------------------------------|\n");

print(' Paciente:',nome,'\n');
#print('Cálculo do IMC: ' + str(f'{v_imc:.2f}') + ' kg/m2.\n');
print(' Cálculo do IMC: ' + v_imc[0:5] + ' kg/m2.\n');
print(c_imc);

print("\n|------------------------------------Fim do programa--------------------------------------|\n");

input(' Pressione enter para finalizar o programa.\n')