import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import datetime
import smtplib
import csv
import re
import datetime 



#connecting the website
url ='https://www.amazon.eg/RTX-4060-2X-8G-%D8%A7%D9%85/dp/B0C8BPW1SP/ref=sr_1_1?crid=25GHKY3ILWLWY&dib=eyJ2IjoiMSJ9.tGccbl6QvtvWU9a8dnfi1tgRRg7ClIqAlp6YzfIXAjkSI41WAC34edOoSJTwz_XIW7dN2IyPjWl9Nxo4B8L9da95crtaldEMXYfUwvm2XCUJRDUV_H0aEk6pp05MpW-NiRiV6IrVaU8Ae5lvEfhehiXtjQa9ANAb4YFD_d44xODdzInnenQVe4C4872Z6Um3kUPYEzous7-boQMU1ltMTg9uZwdOxmDRoNDhEzu95N8Fj0Ts1JoRKnq-dby-FMDNvdICLKeEMb9M2YdBl47tvkJgCPaIxAxpKQ0xW00-AHCqkje6yVGB7WxXFj0AQKeNBboC-zlfMc1zTbzLbCn8CzRHBjYK8t9tgWIlhYeMEXmtY0_qVvIFdLkkO1a5nIzEH9cdqXcJ4d7vAxPBzxHK1fcZOh6VyZW1W6oEI8ac493ja52xAo2cMFjzT8KTQhpx.szNhOKOGHX81rmJV1PQpYCO54800cMPreaX299MeXwc&dib_tag=se&keywords=rtx+5090&qid=1739820902&sprefix=rt%2Caps%2C134&sr=8-1'
headers={ "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36", 
    "X-Amzn-Trace-Id": "Root=1-67b38cea-341c6de70146e140320b7ab3"}




page = requests.get(url,headers=headers)
soup1 = BeautifulSoup(page.content, 'html.parser')
soup2=BeautifulSoup(soup1.prettify(),'html.parser')
title = soup2.find(id='productTitle').get_text(strip=True)
title = title.encode('utf-8', 'ignore').decode('utf-8')


price_whole = soup2.find("span", {"class": "a-price-whole"})
price_decimal = soup2.find("span", {"class": "a-price-decimal"})
price_fraction = soup2.find("span", {"class": "a-price-fraction"})
 
price_whole_text = price_whole.get_text(strip=True) if price_whole else ""
price_decimal_text = price_decimal.get_text(strip=True) if price_decimal else "."
price_fraction_text = price_fraction.get_text(strip=True) if price_fraction else "00"
price = f"{price_whole_text}{price_decimal_text}{price_fraction_text}"
price = re.sub(r"[^\d.,]", "", price)  
today=datetime.date.today()

csv_file = r'C:\Users\loq\Desktop\web scraping\AmazonWebScraperDataset.csv'

# Check if file exists and read its content to check for duplicates
try:
    df = pd.read_csv(csv_file, encoding='utf-8-sig')
    existing_titles = df['title'].tolist()  # List of existing titles in the file
except FileNotFoundError:
    df = pd.DataFrame(columns=["title", "price", "date"])  # Create an empty DataFrame if file doesn't exist
    existing_titles = []

# Only write if the title doesn't already exist
if title not in existing_titles:
    # Writing data to CSV (append mode)
    with open(csv_file, 'a', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        # Write headers only if the file is empty (first time writing)
        f.seek(0, 2)  # Move the file pointer to the end to check if it's empty
        if f.tell() == 0:  # If file is empty, write headers
            writer.writerow(["title", "price", "date"])
        writer.writerow([title, price, today])

# Reading and displaying the CSV file
df = pd.read_csv(csv_file, encoding='utf-8-sig')
print(df) 
def check_price():
    url ='https://www.amazon.eg/RTX-4060-2X-8G-%D8%A7%D9%85/dp/B0C8BPW1SP/ref=sr_1_1?crid=25GHKY3ILWLWY&dib=eyJ2IjoiMSJ9.tGccbl6QvtvWU9a8dnfi1tgRRg7ClIqAlp6YzfIXAjkSI41WAC34edOoSJTwz_XIW7dN2IyPjWl9Nxo4B8L9da95crtaldEMXYfUwvm2XCUJRDUV_H0aEk6pp05MpW-NiRiV6IrVaU8Ae5lvEfhehiXtjQa9ANAb4YFD_d44xODdzInnenQVe4C4872Z6Um3kUPYEzous7-boQMU1ltMTg9uZwdOxmDRoNDhEzu95N8Fj0Ts1JoRKnq-dby-FMDNvdICLKeEMb9M2YdBl47tvkJgCPaIxAxpKQ0xW00-AHCqkje6yVGB7WxXFj0AQKeNBboC-zlfMc1zTbzLbCn8CzRHBjYK8t9tgWIlhYeMEXmtY0_qVvIFdLkkO1a5nIzEH9cdqXcJ4d7vAxPBzxHK1fcZOh6VyZW1W6oEI8ac493ja52xAo2cMFjzT8KTQhpx.szNhOKOGHX81rmJV1PQpYCO54800cMPreaX299MeXwc&dib_tag=se&keywords=rtx+5090&qid=1739820902&sprefix=rt%2Caps%2C134&sr=8-1'
    headers={ "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36", 
    "X-Amzn-Trace-Id": "Root=1-67b38cea-341c6de70146e140320b7ab3"}




    page = requests.get(url,headers=headers)
    soup1 = BeautifulSoup(page.content, 'html.parser')
    soup2=BeautifulSoup(soup1.prettify(),'html.parser')
    title = soup2.find(id='productTitle').get_text(strip=True)
    title = title.encode('utf-8', 'ignore').decode('utf-8')


    price_whole = soup2.find("span", {"class": "a-price-whole"})
    price_decimal = soup2.find("span", {"class": "a-price-decimal"})
    price_fraction = soup2.find("span", {"class": "a-price-fraction"})
 
    price_whole_text = price_whole.get_text(strip=True) if price_whole else ""
    price_decimal_text = price_decimal.get_text(strip=True) if price_decimal else "."
    price_fraction_text = price_fraction.get_text(strip=True) if price_fraction else "00"
    price = f"{price_whole_text}{price_decimal_text}{price_fraction_text}"
    price = re.sub(r"[^\d.,]", "", price)  
    today=datetime.date.today()
    with open(csv_file, 'a', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        # Write headers only if the file is empty (first time writing)
        f.seek(0, 2)  # Move the file pointer to the end to check if it's empty
        if f.tell() == 0:  # If file is empty, write headers
            writer.writerow(["title", "price", "date"])
        writer.writerow([title, price, today])
while(True):
    check_price()
    time.sleep(5)