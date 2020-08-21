import requests
import json
import pprint

accuweatherAPIKey = 'jGB55F01d2EQWnBiFCPeqlra3A7GQIuV';

'''
    imprimindo todas as infos presentes sobre a localização dentro da requisição r
        - print(r.text);

    imprimindo o type, onde se buscarmos somente por r.text, será retornado string, 
    porém, não é uma boa prática e nem podemos trabalhar com informações assim, por isso, 
    importaremos o modulo json e através da função json.loads, passando como parameto o r.text, 
    será retornar que temos um 'dicionário' de dados, facilitando nosso trabalho.
        - print(type(json.loads(r.text)));
    
    mostrados os dados como um dict, porém, sem uma estrutura boa para identificar os dados, 
    para isso usaremos outro modulo do python, chamado pprint, para mostrar de modo organizado, 
    toda aquelas informações do dict
        - print(pprint.pprint(localizacao));

    após processo de organizar tudo que foi coletado, usaremos duas informações para se basear na geolocalização...
    que seria a geoplugin_latitude e geoplugin_longitude
        - lat = localizacao['geoplugin_latitude'];
        - long = localizacao['geoplugin_longitude'];
    
    - verificando se as infos estão imprimindo corretamente:
        - print('Lat:', lat);
        - print('Long:', long);

    - endereço adquirido no cURL:
        - http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey=jGB55F01d2EQWnBiFCPeqlra3A7GQIuV&q=-26.267811%2C%20-48.851475&language=pt-br

        - optei fazer a quebra de linha de toda a url, para ficar mais vísivel e mais facil de manipular a mesma
        durante o desenvolvimento, optei também, em trocar a apikey que estava na url de modo fixo, pela variavel
        declarada la no ínicio, para que ficasse de modo dinâmico, assim, caso em algum momento a mesma for alterada, 
        será de maneira automatica em todo o código.
        - alterei tambem as posições de latitude e longitude, para pegar dinamicamente, as que estão registradas
        nas variaveis geoplugin_latitude e geoplugin_longitude

'''



#função para adquirir e armazenar as informações de localização em um dict
def getCoordinates():
    #requisição HTTP para API do GEOPLUGIN
    r = requests.get('http://www.geoplugin.net/json.gp');


    #verificação do status code
    if (r.status_code != 200):
        print('Não foi possível obter a localização!');
    else:
        #armazenando toda informação da requisição convertida para um dict python(JSON), em uma variavel...
        localizacao = json.loads(r.text);
        #criando um dict vazio, onde cada uma das suas chaves, irá armazenar respectivamente a lat e a long
        coordinates = {};
        coordinates['lat'] = localizacao['geoplugin_latitude'];
        coordinates['long'] = localizacao['geoplugin_longitude'];
        return coordinates;


#função para retornar o nome e o codigo do local, para acessar os dados da previsao
def getLocalCode(lat,long):

    LocationAPIUrl = "http://dataservice.accuweather.com/locations/v1/cities/geoposition/" \
        + "search?apikey=" + accuweatherAPIKey \
        + "&q=" + lat + "%2C%20" + long + "&language=pt-br";

    r = requests.get(LocationAPIUrl);
    if (r.status_code != 200):
        print('Não foi possível obter o código do local!');
    else:
        '''
            essa impressão foi mais para meios de confirmação dos dados, por isso não usaremos mais
            print(pprint.pprint(json.loads(r2.text)));
        '''
        #variavel para converter toda a informação contida no r, para um dict python
        locationResponse = json.loads(r.text);
        #realizando mesmo processo de criação de um dict vazio, porém, aqui irá armazenar as infos locais
        infoLocal = {}
        #variavel para armazenar o nome local e mais algumas informações, do qual pegaremos as informaçoes do clima
        # 1º parte será o bairro da cidade + 2º parte será o nome da cidade + 3º parte será o estado + 4º parte o país
        #agora nomeLocal, passa a ser uma chave do dict
        infoLocal['nomeLocal'] = locationResponse['LocalizedName'] + " - " \
            + locationResponse['ParentCity']['LocalizedName'] + ", " \
            + locationResponse['AdministrativeArea']['LocalizedName'] + ". " \
            + locationResponse['Country']['LocalizedName'];
        #variavel para acessar o codigo do local, que sera repassado para usar na api Current Conditions.
        #transformando a mesma em uma das chaves do dict
        infoLocal['codigoLocal'] = locationResponse['Key'];
        #print("Obtendo clima de:",nomeLocal,"\n");
        #print("Código do Local:",codigoLocal);
        return infoLocal;

def getTimeNow(codigoLocal,nomeLocal):
    #CurrentConditions que irá retornar a temperatura e o 'texto' do clima
    CurrentConditionsAPIUrl = "http://dataservice.accuweather.com/currentconditions/v1/" \
        + codigoLocal + "?apikey=" + accuweatherAPIKey + "&language=pt-br";

    r = requests.get(CurrentConditionsAPIUrl);

    if (r.status_code != 200):
        print('Não foi possível obter as informações com relação ao clima e temperatura!');
    else:
        CurrentConditionsResponse = json.loads(r.text);
        #print(pprint.pprint(CurrentConditionsResponse));
        # novamente realizando mesmo processo de criação de um dict vazio, porém, aqui irá armazenar as infos do clima
        infoClima = {};
        #aqui estaremos tranformando as variaveis em chaves do dict
        infoClima['TextoClima'] = CurrentConditionsResponse[0]['WeatherText'];
        infoClima['Temperatura'] = CurrentConditionsResponse[0]['Temperature']['Metric']['Value'];
        infoClima['nomeLocal'] = nomeLocal;

        #print("Condição climática: " + TextoClima);
        #print("Temperatura: " + str(Temperatura) + "ºC");
        #retornando o dict
        return infoClima;



##        INICIANDO O PROGRAMA

#criando uma variavel para armazenar as informações que seram retornadas ao chamar a função que obtem as coordenadas
coordinates = getCoordinates();

#criando agora uma variavel para armazenar as informações nome e o codigo do local
#vale lembrar que a função getLocalCode, recebe dois parametros, que seram chaves do dict armazenado na var coordinates
local = getLocalCode(coordinates['lat'],coordinates['long']);

#criando a variavel para armazenar o as informações de clima e temperatura atual
#e da mesma forma como no local, a funcao getTimeNow recebe dois parametro, que seram chaves do dict armazenados na var local
currentWeather = getTimeNow(local['codigoLocal'],local['nomeLocal']);

print('\nObtendo clima de: ' + currentWeather['nomeLocal']);
print('Condição climática: ' + currentWeather['TextoClima']);
print('Temperatura: ' + str(currentWeather['Temperatura']) + "\xb0" + "C\n"); #\xb0 -> codigo que representa 'graus'