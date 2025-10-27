import sys
from bs4 import BeautifulSoup, SoupStrainer

filename = sys.argv[1]

with open(filename, 'r', encoding='utf-8') as file:
    html_doc = file.read()

all_tags = SoupStrainer(name=True)

soup = BeautifulSoup(html_doc, 'html.parser', parse_only=all_tags)

for _, tag in enumerate(soup.find_all(True)):
    print(tag)
