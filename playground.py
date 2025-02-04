import requests
import csv
from bs4 import BeautifulSoup


def getcata():
    base = 'https://books.toscrape.com/'
    page = requests.get(base, timeout=10)
    soup = BeautifulSoup(page.content, 'html.parser')

    categories = []

    for cat_link in soup.select('.side_categories ul li ul li a'):
        category_url = base + cat_link["href"] 
        categories.append(category_url)

    for category_url in categories:
        category_page = requests.get(category_url)
        category_soup = BeautifulSoup(category_page.content, 'html.parser')
        
        while category_soup.select_one('.next a'):
            next_page = category_soup.select('.next a')[0]['href']
            next_page_url = base + next_page
            categories.append(next_page_url)
        

            category_page = requests.get(next_page_url)
            category_soup = BeautifulSoup(category_page.content, 'html.parser')
            while category_soup.select_one('.next a'):
                next_page = category_soup.select('.next a')[0]['href']
                next_page_url = base + next_page
                categories.append(next_page_url)

    return(categories)




