# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 13:05:53 2020

@author: truet
"""
import contextlib
import pandas as pd
from concurrent.futures import ThreadPoolExecutor

import bs4
import requests
import time
from requests_html import HTMLSession

def get_soup(url):
    """get soup of url"""
    session = HTMLSession()
    r = session.get(url)
    soup = bs4.BeautifulSoup(r.content, 'lxml')
    return soup

def main():
    url = "https://www.roguefitness.com/weightlifting-bars-plates/barbells?is_salable[0]=1&limit=160"
    soup = get_soup(url)
    container = soup.find_all('li', {'class':'item'})
    results = []
    for c in container:
        product_title = c.find('h2', {'class':'product-name'}).text.strip()
        price = c.find('span', {'class':'price'}).text.strip()
        img_url = c.find('a', 'product-image').img['src']
        url = c.find('a', {'class':'product-image'})['href']
        stock = "In Stock"
        results.append(dict(p_title = product_title, price = price, stock = stock, url = url, 
                            company = "Rogue Fitness", p_type = "Barbells", img_url = img_url))
    results = pd.DataFrame(results)
    return results