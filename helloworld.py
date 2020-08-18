import math

print("|----------O meu primeiro programa em python-----------|\n")

def efetuar_soma(v1,v2):
	a = v1
	b = v2

	return a+b

def efetuar_sub(v1,v2):
	a = v1
	b = v2

	return a-b

def raiz_quadrada(v1):
	raiz = math.sqrt(v1)

	return raiz



Num1 = int(input('Insira o primeiro valor: '))
Num2 = int(input('Insira o segundo valor: '))
Num3 = int(input('Insira o terceiro valor: '))

print("\n|------------------------------------------------------|\n")

soma = efetuar_soma(Num1,Num2)
sub = efetuar_sub(Num1,Num2)
raiz_quad = raiz_quadrada(Num3)

print(" Resultado da soma de",Num1,"+",Num2,"é:",soma)
print("\n Resultado da subtração de",Num1,"-",Num2,"é:",sub)
print("\n Resultado da raiz quadrada de",Num3,"é:",raiz_quad)

print("\n|-------------------Fim do programa--------------------|\n")