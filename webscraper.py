import requests
from bs4 import BeautifulSoup

# The URL of the website you want to scrape
url = 'http://www.bbc.com'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the elements that contain article titles
article_titles = soup.find_all('h3')#change the parts to see what you are trying to scrape!

# Extract and print the text of each article title
for title in article_titles:
    print(title.text)
