import sys
from bs4 import BeautifulSoup, SoupStrainer

filename = sys.argv[1]

with open(filename, 'r', encoding='utf-8') as file:
    html_doc = file.read()

only_a_tags = SoupStrainer("a")

soup = BeautifulSoup(html_doc, 'html.parser', parse_only=only_a_tags)

for link in soup:
    print(link.get('href'))
