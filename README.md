# my_first_web_scraping_project
Amazon Price Tracker

This is a Python web scraping project that tracks the price of a product on Amazon Egypt. The script extracts the product's title and price, stores the data in a CSV file, and updates it periodically.

Features

✅ Scrapes product title and price from Amazon Egypt.✅ Saves the extracted data into a CSV file.✅ Prevents duplicate entries.✅ Runs continuously to track price changes.

Prerequisites

Ensure you have Python installed. Then, install the required dependencies:

pip install requests beautifulsoup4 pandas

How It Works

The script sends a request to the Amazon product page.

It extracts the product title and price using BeautifulSoup.

The data is saved in a CSV file (AmazonWebScraperDataset.csv).

The script runs in a loop to check the price every few seconds.

Usage

Run the script using:

python amazon_price_tracker.py

File Structure

📂 Amazon-Price-Tracker
 ├── amazon_price_tracker.py   # Main script
 ├── AmazonWebScraperDataset.csv # Stores extracted data
 ├── README.md                # Project documentation
 ├── requirements.txt         # List of dependencies

Future Improvements

Add error handling for failed requests.

Store data in a database instead of a CSV file.

Send email notifications when prices drop.

License

This project is open-source. Feel free to modify and improve it! 🚀
