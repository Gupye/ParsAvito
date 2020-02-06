import csv

import requests

from get_image_avito import tel_avito
from scan_num import number_scan

try:
    from PIL import Image
except ImportError:
    import Image
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    q = r.text
    return (q)


def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    pages = soup.find('div', class_='pagination-pages').find_all('a', class_='pagination-page')[-1].get('href')
    total_pages = pages.split('=')[1].split('&')[0]
    return int(total_pages)


def write_csv(data):
    with open('avito.csv', 'a', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow((data['title'],
                         data['price'],
                         data['address'],
                         data['url'],
                         data['number']))


def get_page_data(html, file_read, file_have):
    soup = BeautifulSoup(html, 'lxml')
    ads = soup.find('div', class_='js-catalog_serp').find_all('div', class_='item_table')
    for ad in ads:
        try:
            url = 'https://www.avito.ru' + ad.find('div', class_='snippet-title-row').find('h3').find('a').get(
                'href').strip()

        except:
            url = ''
        if file_have:
            if url in file_read:
                print('Элемент есть в базе')
                continue
            else:
                print(url)
        try:
            title = ad.find('div', class_='snippet-title-row').find('h3').text.strip()
            print(title)
        except:
            title = ''

        try:
            price = ad.find('div', class_='about').find('span', class_='price').text.strip()
            print(price)
        except:
            price = ''
        try:
            address = ad.find('div', class_='address').find('span', class_='item-address__string').text.strip()
            print(address)
        except:
            address = ''

        tel_avito(url, address)
        number = number_scan()
        print(number)

        data = {'title': title,
                'url': url,
                'price': price,
                'address': address,
                'number': number}
        write_csv(data)


def main():
    base_url = 'https://www.avito.ru/simferopol/kvartiry/prodam?cd=1&user=1&'
    page_part = 'p='
    total_pages = get_total_pages(get_html(base_url))
    try:
        with open('avito.csv', 'r') as f:
            file_read = f.read()
            f.close()
            file_have = True
    except:
        file_have = False
        file_read = ''
    for i in range(1, total_pages + 1):
        url_gen = base_url + page_part + str(i)
        html_url_gen = get_html(url_gen)
        get_page_data(html_url_gen, file_read, file_have)


if __name__ == '__main__':
    main()