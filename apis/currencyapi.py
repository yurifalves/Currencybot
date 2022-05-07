from typing import Union
import time
import requests


inicio = time.time()
def currency_api(date: str, endpoint: str, minified: bool = True, apiVersion: int = 1) -> Union[dict, str]:
    """
    Currency-api: https://github.com/fawazahmed0/currency-api#

    :param date: Data no formato 'YYYY-MM-DD' ou 'latest'. (2020-11-22 É a data mínima para funcionamento da API)
    :param endpoint: Endpoint desejado.
    'currencies' --> Todas as moedas disponíveis, Ex: usd, eur, brl, ...
    'currencies/{currencyCode}' --> lista as moedas com {currencyCode} como moeda base
    'currencies/{currencyCode1}/{currencyCode2}' --> valor da moeda {currencyCode1} em {currencyCode2}
    :param minified: Determina se a versão será minificada(True) ou não(False).
    :param apiVersion: Versão da API. (apenas versão 1 disponível até o momento)

    :return: Dicionário com os dados em json já convertidos. Ou no caso de erro, uma string com o resultado da requisição
    """
    if minified:
        url_structure = f'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@{apiVersion}/{date}/{endpoint}.min.json'
    else:
        url_structure = f'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@{apiVersion}/{date}/{endpoint}.json'

    r = requests.get(url_structure)
    if r.ok:  # status_code < 400
        return r.json()
    else:
        return f'Algo inesperado ocorreu: {r}'


def currency_api_all():
    all_currencies = currency_api('latest', 'currencies')
    all_currencies.pop('brl')
    qtd_moedas = len(all_currencies)
    texto = f'{qtd_moedas} Moedas encontradas\n\n'
    moedas_importantes = ['usd', 'eur', 'gbp', 'chf', 'jpy', 'rub', 'aud', 'cad', 'ars']
    moedas_secundarias = [codigo for codigo in all_currencies.keys() if codigo not in moedas_importantes]

    while len(moedas_importantes) != 0:
        codigo = moedas_importantes[0]
        moeda = all_currencies[codigo]
        cotacao, data = currency_api('latest', f'currencies/{codigo}/brl')['brl'], currency_api('latest', f'currencies/{codigo}/brl')['date']
        texto += f'{moeda} ({codigo.upper()}) = R$ {cotacao}   [{data}]\n'
        moedas_importantes.remove(codigo)

    for codigo, moeda in all_currencies.items():
        cotacao, data = currency_api('latest', f'currencies/{codigo}/brl')['brl'], currency_api('latest', f'currencies/{codigo}/brl')['date']
        texto += f'{moeda} ({codigo.upper()}) = R$ {cotacao}   [{data}]\n'

    with open('meuarquivo12345.txt', 'w', encoding='utf-8') as arquivo:
        arquivo.write(texto)

    arquivo = open('meuarquivo12345.txt', 'r')
    return arquivo

if __name__ == '__main__':
    currency_api_all()


print(time.time()-inicio)
