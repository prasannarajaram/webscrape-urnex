# webscrape-urnex
## Purpose
Scraping ingredients PDF files from urnex.com/sds

## How to use this
1. Download (or clone) this repository
2. Run the urnex_scrape.py file
3. The same directory should have the all the ingredient files downloaded (107 files as of this writing)

## Planned improvements
1. Download by product category into seperate folders
2. Create an Excel file with category-wise separation to individual downloaded files
3. Add GUI using PyQt5 to allow download in particular directory. Show in dialog the count of different types of ingredient files downloaded with overall count
   For example: 
   URNEX-COMMERCIAL - 10 files downloaded
   CO-BRANDED PORTFOLIO - 16 files downloaded
   Total 98 files downloaded
