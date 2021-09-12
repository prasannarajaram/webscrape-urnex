import os
import pdb
import requests


def createsubdir(subdir):
    try:
        parent_main = os.getcwd()
        newpath = os.path.join(parent_main, subdir)
        # pdb.set_trace()
        os.mkdir(newpath)
        print(f'{newpath} created')
        os.chdir(newpath)
        # pdb.set_trace()
    except FileExistsError:
        os.chdir(subdir)
        print(f"Info: Not creating '{subdir}' directory. It already exists")
    return(parent_main)


def createproddir(subdir):
    try:
        parent = os.getcwd()
        newpath = os.path.join(parent, subdir)
        os.mkdir(newpath)
        print(f'{newpath} created')
    except FileExistsError:
        print(f"Info: Not creating '{subdir}' directory. It already exists")


def download_file(parent_main, subdir, proddir, pdf_link):
    newpath = os.path.join(parent_main, subdir, proddir)
    os.chdir(newpath)
    filename = pdf_link.split('/')[-1]
    print(f'Downloading file to {proddir} {filename}')
    response = requests.get(pdf_link)
    pdf = open(filename, 'wb')
    pdf.write(response.content)
    pdf.close()
