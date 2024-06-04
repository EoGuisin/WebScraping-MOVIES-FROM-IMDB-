import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm"

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
movies = soup.find_all('div', class_='sc-7630d22e-3 kssHlQ ipc-page-grid__item ipc-page-grid__item--span-2')

with open ('movies.csv', 'a', newline='', encoding='utf8') as file:
    for movie in movies:
        movieName = movie.find('h3', class_='ipc-title__text').get_text()
        movieInfo = movie.find('div', class_='sc-b189961a-7 feoqjK cli-title-metadata')
        movieInfo = movieInfo.get_text(separator=' ')

        line = f'{movieName} - Informations: {movieInfo} \n'
        file.write(line)
