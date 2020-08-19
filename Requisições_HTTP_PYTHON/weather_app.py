import requests
import json
import pprint

accuweatherAPIKey = 'jGB55F01d2EQWnBiFCPeqlra3A7GQIuV';

#requisição HTTP para API do GEOPLUGIN
r = requests.get('http://www.geoplugin.net/json.gp');


#verificação do status code
if (r.status_code != 200):
    print('Não foi possível obter a localização!');
else:
    '''
        imprimindo todas as infos presentes sobre a localização dentro da requisição r
            - print(r.text);

        imprimindo o type, onde se buscarmos somente por r.text, será retornado string, 
        porém, não é uma boa prática e nem podemos trabalhar com informações assim, por isso, 
        importaremos o modulo json e através da função json.loads, passando como parameto o r.text, 
        será retornar que temos um 'dicionário' de dados, facilitando nosso trabalho.
            - print(type(json.loads(r.text)));

    '''

    #armazenando toda informação da requisição convertida para um dict python(JSON), em uma variavel...
    localizacao = json.loads(r.text);

    '''
        mostrados os dados como um dict, porém, sem uma estrutura boa para identificar os dados, 
        para isso usaremos outro modulo do python, chamado pprint, para mostrar de modo organizado, 
        toda aquelas informações do dict

        após esse processo, usaremos duas informações para se basear na geolocalização...
        que seria a geoplugin_latitude e geoplugin_longitude

        print(pprint.pprint(localizacao));

    '''

    lat = localizacao['geoplugin_latitude'];
    long = localizacao['geoplugin_longitude'];

    

    '''
    - verificando se as infos estão imprimindo corretamente:
        - print('Lat:', lat);
        - print('Long:', long);


    - endereço adquirido no cURL:
        - http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey=jGB55F01d2EQWnBiFCPeqlra3A7GQIuV&q=-26.267811%2C%20-48.851475&language=pt-br

    '''

    '''
        - optei fazer a quebra de linha de toda a url, para ficar mais vísivel e mais facil de manipular a mesma
        durante o desenvolvimento, optei também, em trocar a apikey que estava na url de modo fixo, pela variavel
        declarada la no ínicio, para que ficasse de modo dinâmico, assim, caso em algum momento a mesma for alterada, 
        será alterada automaticamente em todo o código.
        - alterei tambem as posições de latitude e longitude, para pegar dinamicamente, as que estão registradas
        nas variaveis geoplugin_latitude e geoplugin_longitude
    '''
    LocationAPIUrl = "http://dataservice.accuweather.com/locations/v1/cities/geoposition/" \
        + "search?apikey=" + accuweatherAPIKey \
        + "&q=" + lat + "%2C%20" + long + "&language=pt-br";

    r2 = requests.get(LocationAPIUrl);
    if (r2.status_code != 200):
        print('Não foi possível obter o código do local!');
    else:
        '''
            essa impressão foi mais para meios de confirmação dos dados, por isso não usaremos mais
            print(pprint.pprint(json.loads(r2.text)));
        '''
        #variavel para converter toda a informação contida no r2, para um dict python
        locationResponse = json.loads(r2.text);
        #variavel para armazenar o nome local e mais algumas informações, do qual pegaremos as informaçoes do clima
        # 1º parte será o bairro da cidade + 2º parte será o nome da cidade + 3º parte será o estado + 4º parte o país
        nomeLocal = locationResponse['LocalizedName'] + " - " \
            + locationResponse['ParentCity']['LocalizedName'] + ", " \
            + locationResponse['AdministrativeArea']['LocalizedName'] + ". " \
            + locationResponse['Country']['LocalizedName'];
        #variavel para acessar o codigo do local, que sera repassado para usar na api Current Conditions.
        codigoLocal = locationResponse['Key'];
        print("Local:",nomeLocal);
        print("Código do Local:",codigoLocal);