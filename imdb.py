import requests
from bs4 import BeautifulSoup
from random import randint


class MeuRobo():

    def get_site(self):
        response = requests.get(
            'https://www.imdb.com/chart/top/?ref_=nv_mv_250',
            headers={'Accept-Language': 'en-US,en;q=0.9'},
        )
        response.raise_for_status()

        parsed_html = BeautifulSoup(response.content, 'lxml')

        filmes = []
        for item in parsed_html.select('li.ipc-metadata-list-summary-item'):
            nome_el = item.select_one('h3.ipc-title__text')
            ano_el = item.select_one('span.cli-title-metadata-item')
            if not nome_el:
                continue
            nome = nome_el.get_text(strip=True)
            # Strip the rank prefix "1. ", "2. ", etc.
            if '. ' in nome:
                nome = nome.split('. ', 1)[1]
            ano = ano_el.get_text(strip=True) if ano_el else ''
            filmes.append({'Nome do Filme': nome, 'Ano': ano})

        return filmes


if __name__ == '__main__':
    a = MeuRobo()
    filmes = a.get_site()
    print(filmes[randint(0, len(filmes) - 1)])
