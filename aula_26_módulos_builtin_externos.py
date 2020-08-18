import time as t;
import matplotlib.pyplot as plt;
import random;

palavras = ['Belicoso','Temperança','Corolário','Aurir','Porfiar','Deferido'];

escolha = random.choice(palavras);

print(' Palavra escolhida aleatoriamente para digitar é: ' + escolha);

tentativas = [];
vez = 1
tempos = [];
legenda = [];
repetir = 5

print('\n ESTE PROGRAMA IRÁ MARCAR O TEMPO DE DIGITAÇÃO DE UMA PALAVRA ESCOLHIDA DE MANEIRA RANDOMICA.\n VOCÊ TERÁ QUE DIGITAR A MESMA ' + str(repetir) + ' VEZES E O PROGRAMA IRÁ REGISTRAR OS TEMPOS.\n');
input(' Aperte enter para iniciar..');

while vez <= repetir:

    inicio = t.perf_counter();
    input('Insira a palavra: ');
    fim = t.perf_counter();

    tempo_total = round(fim - inicio,2);

    tempos.append(tempo_total);
    tentativas.append(vez);
    vez_legenda = str(vez) + 'º vez';
    legenda.append(vez_legenda);
    vez += 1;

plt.xticks(tentativas,legenda);

plt.plot(tentativas,tempos)

plt.show();

print('|----------------------------------Fim do programa!----------------------------------|')