"""
Przykład użycia biblioteki Scrapy do pobierania danych o nowych serialach z Filmweb.
Spider pobiera tytuł, gatunki oraz rok produkcji dla każdego serialu.
"""

import scrapy
import logging

# Ustawienie poziomu logowania, by wyświetlać jedynie istotne komunikaty
logging.getLogger('scrapy').setLevel(logging.WARNING)

class FilmwebPremiereSpider(scrapy.Spider):
    name = "filmweb_premiere"
    start_urls = ['https://www.filmweb.pl/ranking/premiere/serial']

    def parse(self, response):
        for element in response.css('div.rankingType'):
            title = element.css('div.rankingType__titleWrapper a::text').get()
            title = title.strip() if title else "brak tytułu"

            genres = element.css('div.rankingType__genres a.tag.rankingGerne span::text').getall()
            genres_str = ', '.join([g.strip() for g in genres]) if genres else "brak gatunków"

            year = element.css('span.rankingType__year::text').get()
            year = year.strip() if year else "brak roku"

            yield {
                'title': title,
                'genres': genres_str,
                'year': year
            }
