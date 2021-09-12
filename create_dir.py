import os
import requests
import logging
logging.basicConfig(filename='download.log', encoding='utf-8', level=logging.DEBUG)

def createsubdir(subdir):
    try:
        parent_main = os.getcwd()
        newpath = os.path.join(parent_main, subdir)
        os.mkdir(newpath)
        logging.info('%s created', newpath)
        os.chdir(newpath)
    except FileExistsError:
        os.chdir(subdir)
        logging.info("Not creating '%s' directory. It already exists", subdir)
    return(parent_main)


def createproddir(proddir):
    try:
        parent = os.getcwd()
        newpath = os.path.join(parent, proddir)
        os.mkdir(newpath)
        logging.info('%s created', newpath)        
    except FileExistsError:
        logging.info("Not creating '%s' directory. It already exists", proddir)        


def download_file(parent_main, subdir, proddir, pdf_link):
    newpath = os.path.join(parent_main, subdir, proddir)
    os.chdir(newpath)
    filename = pdf_link.split('/')[-1]
    logging.info("Downloading file to %s %s", proddir, filename)
    response = requests.get(pdf_link)
    pdf = open(filename, 'wb')
    pdf.write(response.content)
    pdf.close()
