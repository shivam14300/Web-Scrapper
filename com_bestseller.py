import requests
import csv
from bs4 import BeautifulSoup
name = ["Name"]
urls = ["URL"]
author = ["Author"]
price = ["Price"]
no_rating = ["Number of Rating"]
avg_rating = ["Average Rating"]
page = 1
while page <= 5:
    page_no = str(page)
    url1 = "https://www.amazon.com/"
    url2 = "best-sellers-books-Amazon/zgbs/books/ref = zg_bs_pg_"
    url3 = "/138-8010109-3540328?_encoding = UTF8&pg = "
    url = url1 + url2 + page_no + url3 + page_no
    source_code = requests.get(url)
    soup = BeautifulSoup(source_code.content, "lxml")
    for link1 in soup.findAll('div', {'class': 'zg_itemImmersion'}):
        href = link1.find('a')
        if href:
            ur = 'https://www.amazon.com' + href.get('href')
            urls.append(ur)
        else:
            urls.append("Not available")
        link = link1.find('div',{'class': 'p13n-sc-truncate p13n-sc-line-clamp-1'})
        if link:
            title = link.getText()
            name.append(title)
        else:
            name.append("Not available")
        link = link1.find('a', {'class': 'a-size-small a-link-child'})
        if link:
            aut = link.getText()
            author.append(aut)
        else:
            author.append("Not available")
        link = link1.find('a', {'class': 'a-link-normal a-text-normal'})
        if link:
            pri = link.getText()
            price.append(pri)
        else:
            price.append("Not available")
        link = link1.find('a', {'class': 'a-size-small a-link-normal'})
        if link:
            nr = link.getText()
            no_rating.append(nr)
        else:
            no_rating.append("Not available")
        link = link1.find('div', {'class': 'a-icon-row a-spacing-none'})
        if link:
            link2 = link.find('a', {'class': 'a-link-normal'})
            if link2:
                avr = link2.getText()
                avg_rating.append(avr)
            else:
                avg_rating.append("Not available")
        else:
            avg_rating.append("Not available")
    page += 1

rows = zip(name, urls, author, price, no_rating, avg_rating)
csvfile = "./output/com_book.csv"
with open(csvfile, "w") as output:
    write = csv.writer(output, delimiter=';')
    for row in rows:
        write.writerow(row)
