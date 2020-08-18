import matplotlib.pyplot as plt

'''
    no eixo x do grafico, ficará os meses, porém, na listagem não
    é aceito strings, mas posteriormente será feito legenda.   
'''

x = [1,2,3,4,5,6,7];
y = [1500,1800,2100,1300,1900,2200,2000];

plt.plot(x,y);

legendas = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho'];

plt.xticks(x,legendas);

plt.plot(x,y)

plt.show();