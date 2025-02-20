# My First Web Scraping Project  

This is a simple **Python** web scraping project that tracks product prices on **Amazon Egypt**. The script extracts the product's title and price, then saves the data in a **CSV** file with periodic updates.  

## ✨ Features  

✅ Extracts the product title and price from Amazon Egypt.  
✅ Stores the extracted data in a CSV file.  
✅ Prevents duplicate entries.  
✅ Automatically updates prices periodically.  

## 📌 Prerequisites  

Make sure you have **Python** installed on your system. Then, install the required libraries using the following command:  

```bash
pip install requests beautifulsoup4 pandas
⚙️ How It Works
The script sends a request to the Amazon product page.
It uses BeautifulSoup to extract the title and price.
The data is saved in a AmazonWebScraperDataset.csv file.
The script runs in a loop to check the price every few seconds.
▶️ Usage
Run the script using the following command:

bash
Copy
Edit
python my_first_web_scraping.py
📁 File Structure
plaintext
Copy
Edit
📂 My-first-web-scraping  
├── my_first_web_scraping.py     # Main script  
├── AmazonWebScraperDataset.csv  # Stores extracted data  
├── README.md                    # Project documentation  
├── requirements.txt             # List of dependencies  
