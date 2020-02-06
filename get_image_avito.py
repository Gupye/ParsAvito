import base64
import os
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
import wget

driver = webdriver.Chrome('chromedriver.exe')


def tel_avito(url, address):
    driver.get(url)
    sleep(1)
    button = driver.find_element_by_xpath('//a[@class="button item-phone-button js-item-phone-button button-origin '
                                          'button-origin-blue button-origin_full-width button-origin_large-extra '
                                          'item-phone-button_hide-phone item-phone-button_card '
                                          'js-item-phone-button_card"]')
    button.click()
    sleep(1)
    soup = BeautifulSoup(driver.page_source, 'lxml')

    os.makedirs('Фото с Авито/{}'.format(address), exist_ok=True)
    img_avito(soup, address)
    stra = soup.find('div', class_='item-phone-big-number').find('img').get('src').split(',')[-1]

    with open("num.jpg", "wb") as new_file:
        new_file.write(base64.decodebytes(stra.encode()))


def img_avito(html_soup, outd):
    imgs = html_soup.find('div', class_='gallery-imgs-container js-gallery-imgs-container').find_all('div',
                                                                                                     class_='gallery-img-frame js-gallery-img-frame')
    output_directory = 'Фото с авито/' + outd
    for img in imgs:
        a = img.get('data-url')
        url = 'http:' + a
        filename = wget.download(url, out=output_directory)