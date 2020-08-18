'''

Crie um dicionario de cores em inglês. Em seguida, peça
ao usuário para digitar uma cor em português. Caso exista a cor no dicionário,
imprima a tradução, caso contrário, imprima algo como
"Esta cor não consta no meu dicionário".

'''

print("\n|------------------Dicionário de Cores-------------------|\n\n")


cores = {'vermelho': 'red','verde': 'green','azul': 'blue','branco': 'white','rosa': 'pink','amarelo': 'yellow','preto': 'black'}

'''
para evitar a questão de letras maiusculas e minusculas como entrada nas cores
pelo usuario, faremos a verificação no input, para que tudo que o usuario
inserir seja alterado para minusculo
'''
cor = input('Insira uma cor, para pesquisar a tradução em nosso dicionario: ').lower()

print("\n\n|---------------------------------------------------------|\n")

traducao = cores.get(cor,"Esta cor não consta no meu dicionário")

print("|------------- Cor:",cor,"| tradução:",traducao,"-------------|")

print("\n|--------------------Fim do programa----------------------|\n")

input('Pressione enter para finalizar o programa.\n')