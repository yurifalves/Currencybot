from typing import Union
import requests


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


if __name__ == '__main__':
    print(currency_api('2020-11-22', 'currencies'))
    print(currency_api('2020-11-22', 'currencies/brl'))
    print(currency_api('2020-11-22', 'currencies/usd/brl'))
