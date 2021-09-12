import requests
from bs4 import BeautifulSoup
import create_dir
import pdb
import os


url = "https://urnex.com/sds"

subdir = "downloads"
parent_main = create_dir.createsubdir(subdir)

# Fetch the contents of webpage
page = requests.get(url)
soup = BeautifulSoup(page.content, "lxml")

#class = sds
sds = soup.find_all(class_='sds')
# print(type(sds)) # bs4.element.ResultSet

# sds[1] picks the 2nd occurence of SDS - which matches with ingredients
link = sds[1].find_all('a')
category = sds[1].find(class_='cats')
cats_list = category.find_all('li')
product = []

# Get the list of products in a list
for cats in cats_list:
    if cats.attrs != {}:
        for child in list(cats.children):
            child = str(child).strip().replace(' - ', '_').replace(' ','_')
            create_dir.createproddir(child)
            product.append(child)

# Extract all the <li> tags with data-category-type
# Download the file to the respective directory
link = sds[1].find(class_="files msds-list list-wrapper")
data_cat_type = link.find_all('li')
for data_cat in data_cat_type:
    data_cat_num = data_cat.get('data-category-type')
    if (data_cat_num == '45'):
        proddir = 'Urnex_Commercial'
        pdf_link = data_cat.find('a').get('href')
        create_dir.download_file(parent_main, subdir, proddir, pdf_link)

    elif (data_cat_num == '48'):
        proddir = 'Co-Branded_Portfolio'
        pdf_link = data_cat.find('a').get('href')
        create_dir.download_file(parent_main, subdir, proddir, pdf_link)

    elif (data_cat_num == '44'):
        proddir = 'Urnex_Household'
        pdf_link = data_cat.find('a').get('href')
        create_dir.download_file(parent_main, subdir, proddir, pdf_link)

    elif (data_cat_num == '43'):
        proddir = 'Puro_Commercial'
        pdf_link = data_cat.find('a').get('href')
        create_dir.download_file(parent_main, subdir, proddir, pdf_link)

    elif (data_cat_num == '41'):
        proddir = 'Biocaf_Household'
        pdf_link = data_cat.find('a').get('href')
        create_dir.download_file(parent_main, subdir, proddir, pdf_link)

    elif (data_cat_num == '42'):
        proddir = 'Biocaf_Commercial'
        pdf_link = data_cat.find('a').get('href')
        create_dir.download_file(parent_main, subdir, proddir, pdf_link)
