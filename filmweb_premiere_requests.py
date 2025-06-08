"""
Przykład pobierania nowych premier filmowych z Filmweb przy użyciu bibliotek:
- requests: pobiera stronę HTML,
- BeautifulSoup: parsuje i ekstraktuje dane z HTML.

Dla każdego filmu wyświetlane są tytuł, gatunki oraz rok produkcji.
"""

import requests
from bs4 import BeautifulSoup

def main():
    url = 'https://www.filmweb.pl/ranking/premiere'
    response = requests.get(url)
    response.raise_for_status()  # upewnij się, że strona została pobrana poprawnie

    soup = BeautifulSoup(response.text, 'html.parser')

    # Znajdź wszystkie elementy odpowiadające tytułom filmów
    title_wrappers = soup.find_all('div', class_='rankingType__titleWrapper')

    print("Nowe premiery filmów na Filmweb:")
    for wrapper in title_wrappers:
        title = wrapper.get_text(strip=True)
        parent = wrapper.parent

        # Pobierz gatunki filmowe
        genre_tags = parent.find_all('a', class_='tag rankingGerne')
        genres = [tag.get_text(strip=True) for tag in genre_tags]
        genres_str = ', '.join(genres) if genres else "brak gatunków"

        # Pobierz rok produkcji
        year_tag = parent.find('span', class_='rankingType__year')
        year = year_tag.get_text(strip=True) if year_tag else "brak roku"

        print(f"- {title} | Gatunki: {genres_str} | Rok: {year}")

if __name__ == '__main__':
    main()
