import requests
import json
import pprint

#requisição HTTP para API do GEOPLUGIN
r = requests.get('http://www.geoplugin.net/json.gp');


#verificação do status
if (r.status_code != 200):
    print('Não foi possível obter a localização!');
else:
    localizacao = json.loads(r.text);
    long = localizacao['geoplugin_longitude'];
    lat = localizacao['geoplugin_latitude'];
    #print(pprint.pprint(localizacao));
    print('lat:', lat);
    print('long:', long);