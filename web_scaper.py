import requests
from bs4 import BeautifulSoup
import csv

# URL of the website to scrape
url = 'https://www.asianfanfics.com/'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Data list to store scraped items
data = []

# Find all items with the class 'item' and extract the title and price
for item in soup.find_all('div', class_='item'):
    try:
        title = item.find('h2').text.strip()  # Extract and clean the title
        price = item.find('span', class_='price').text.strip()  # Extract and clean the price
        data.append([title, price])  # Add the data to the list
    except AttributeError:
        # Skip items missing title or price
        continue

# Save the scraped data to a CSV file
with open('data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Price'])  # Write the header row
    writer.writerows(data)  # Write the data rows

print(f"Scraped data saved to 'data.csv' with {len(data)} entries.")
