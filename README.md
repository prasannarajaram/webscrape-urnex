# webscrape-urnex
## Purpose
Scraping ingredients PDF files from urnex.com/sds

## How to use this
1. Download (or clone) this repository
2. Run the urnex_scrape.py file
3. The script will download all the ingredients (PDF files) to the same directory (107 files, as 06-Sep-2021)

## Planned improvements
1. Download product category into seperate folders
2. Create an Excel file with category-wise separation to individual downloaded files
3. Add GUI using PyQt5 to allow download into a particular directory. In a dialog, show the count of different types of ingredient files downloaded with overall count.  
     For example:      
     a. URNEX-COMMERCIAL - 10 files downloaded  
     b. CO-BRANDED PORTFOLIO - 16 files downloaded  
     c. Total 98 files downloaded
