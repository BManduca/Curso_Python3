import time;

def cont_tempo():
    #inicio = time.process_time();
    inicio = time.perf_counter();
    input('Insira o seu nome completo: ');
    #fim = time.process_time();
    fim = time.perf_counter();
    #função round é nativa do python e serve para arrendonda valores float, passando como segundo parametro a quantidade de casas
    tempo_total = round(fim - inicio,2);
    print('Você demorou ' + str(tempo_total) + ' segundos para digitar seu nome completo.')

cont_tempo();