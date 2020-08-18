'''

Criar 3 variaveis:

nome
sobrenome_mae
sobrenome_pai

Em seguida, crie uma variavel chamada iniciais e faça com que ela receba as iniciais do seu nome usando 
índices. No meu caso, por exemplo o valor da váriavel seria bmp.


'''

print("|--------Imprimindo iniciais do nome através dos índices---------|\n")


nome = "Brunno"

sobrenome_mae = "Manduca"

sobrenome_pai = "Prado"

iniciais = nome[:1] + sobrenome_mae[:1] + sobrenome_pai[:1]

completo = nome + ' ' + sobrenome_mae + ' do ' + sobrenome_pai

print(" Iniciais:",iniciais)
print("\n Nome completo:",completo)


print("\n|-------------------------FIM DO PROGRAMA------------------------|")