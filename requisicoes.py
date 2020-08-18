import requests

'''


esse é o processo exatamente que o navegador faz quando digita o endereço
no campo onde vai a url do navegador... é enviado a requisição HTTP para o endereço

para saber qual o status da requisição, é so utilizar a função status...por exemplo:

'variavel'.status_code

-> se caso o status voltar 200: quer dizer que o HTTP Status Code, deu OK ou que a requisição foi bem sucedida....
que foi enviado e recebida a resposta...


existe o HTTP Status Code 403 - Forbidden, que significa que pode ser protegido por senha ou não enviou a senha ou ainda
inseriu a senha errada.

existe o HTTP Status Code 404 - Que significa que o endereço não foi encontrado (Not found).

- a função headers ou r.headers devolve algumas informações sobre a solicitação.

- a função text ou r.text -> devolve todo o codigo HTML da página passada na solicitação

as requisições HTTP não servem somente apenas para pegar dados em um determinado site, podem servir
também, para fazer transferẽncias de dados para qualquer próposito na internet 


'''



r = requests.get('https://www.google.com');

r.status_code

r.headers

r.text