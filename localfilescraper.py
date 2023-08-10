from bs4 import BeautifulSoup

# Specify the path to your local HTML file
html_file_path = 'hello.html'

# Read the contents of the HTML file
with open(html_file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find and print the text within all <p> tags
paragraphs = soup.find_all('body')
for paragraph in paragraphs:
    print(paragraph.text)


