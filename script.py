import requests
from bs4 import BeautifulSoup



def getcata():
    base = 'https://books.toscrape.com/'
    page = requests.get(base)
    soup = BeautifulSoup(page.content, 'html.parser')

    categories = []


    for cat_link in soup.select('".side_categories ul li ul li a"'):
            category_url = base + cat_link["href"] 
            categories.append(category_url)

    return(categories) 



def book_selector(categories):

    for url in categories:
        print(url)

        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        book = []

        for book_link in soup.select("#default > div > div > div > div > section > div:nth-child(2) > ol > li:nth-child(6) > article > h3 > a"):
                book_url = base + book_link['href'] 
                book.append(book_url)


    print(book) 

categories = getcata()
book = book_selector(categories)





def details(book_info):
    upc = soup.find_all('td')
    lefttable = soup.find_all('th')
    title = soup.find('h1')
    desc = soup.select_one('#content_inner > article > p')
    img = soup.select_one('#product_gallery > div > div > div > img')
    fullimgurl = "https://books.toscrape.com/" + img


print(url)
print(title.string)
for result, result2 in zip(lefttable, upc):
    print(result.string+': '+ result2.string)
print(desc.string)
print(img)

#print(upc.string)
