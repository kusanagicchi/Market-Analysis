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


def book_selector(categories):

    book = []
    for url in categories:
        #print(url)

        page = requests.get(url, timeout=10)
        soup = BeautifulSoup(page.content, 'html.parser')
        base = 'https://books.toscrape.com/catalogue'
        

        for book_link in soup.select('.product_pod h3 a'):
                book.append(base + book_link['href'].replace('../../..', ''))
    
    return(book)

def book_details(book):

    for url in book:
        #print(url)

        page = requests.get(url, timeout=10)
        soup = BeautifulSoup(page.content, 'html.parser')
        

        upc = soup.find_all('td')
        lefttable = soup.find_all('th')
        title = soup.find('h1')
        desc = soup.select_one('#content_inner > article > p')
        img = soup.select_one('#product_gallery > div > div > div > img')
        #fullimgurl = "https://books.toscrape.com/" + img

        print(url)
        print(title.string)
        for result, result2 in zip(lefttable, upc):
            print(result.string+': '+ result2.string)  
        print(f"Description: {desc.get_text(strip=True) if desc else 'No description available'}")
             
        print(img)

   

categories = getcata()
book = book_selector(categories)
book_details(book)

