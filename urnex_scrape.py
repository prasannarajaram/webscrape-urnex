import requests
from bs4 import BeautifulSoup

url = "https://urnex.com/sds"

# Fetch the contents of webpage
page = requests.get(url)
soup = BeautifulSoup(page.content, "lxml")

#class = sds
sds = soup.find_all(class_='sds')
# print(type(sds)) # bs4.element.ResultSet

# sds[1] picks the 2nd occurence of SDS - which matches with ingredients
link = sds[1].find_all('a')
# print(type(link)) # bs4.element.ResultSet

# Loop through the ResultSet
# 'find_all' does not work with ResultSet
filecount = 1
for href in link:
    filename = ''
    # print(href.get('href'))
    pdf_link = href.get('href')
    # print(type(pdf_link))
    if ('https' in pdf_link):
        filename = pdf_link.split('/')[-1]
        print(f'Downloading file:{filecount} {filename}')
        response = requests.get(pdf_link)
        pdf = open(filename, 'wb')
        pdf.write(response.content)
        pdf.close()
        filecount += 1
    
    # pdf_file = requests.get(pdf_link)
    # print(pdf_link)
