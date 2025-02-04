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
        

        righttable = soup.find_all('td')
        lefttable = soup.find_all('th')
        title = soup.find('h1')
        desc = soup.select_one('#content_inner > article > p')
        img = soup.select_one('#product_gallery > div > div > div > img')
        #fullimgurl = "https://books.toscrape.com/" + img

        print(url)
        print(title.string)
        
        print(f"Description: {desc.get_text(strip=True) if desc else 'No description available'}")
             
        print(img)

categories = getcata()
book = book_selector(categories)
book_details(book)

