import requests

#requisição HTTP para API do GEOPLUGIN
r = requests.get('http://www.geoplugin.net/json.gp');


#verificação do status
if (r.status_code != 200):
    print('Não foi possível obter a localização!');
else:
    print(r.text);