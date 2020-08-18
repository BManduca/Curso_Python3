'''

Criar 3 variáveis

empresa

nome

sobrenome_pai

em seguida, crie uma variável chamada email. Está variável deve criar um endereço de e-mail
para a pessoa, que deve ter o seguinte formato 'brunno.prado@totvs.com.br'. Use a concatenação para fazer isto


'''

print("|---------------Imprimindo email completo da empresa--------------|\n")

empresa = "TOTVS"

nome = "Brunno"

sobrenome_pai = "Prado"

aux = nome + '.' + sobrenome_pai + '@' + empresa + '.com.br'
email = aux.lower()

print(' Email:',email)

print("\n|-------------------------FIM DO PROGRAMA------------------------|")
