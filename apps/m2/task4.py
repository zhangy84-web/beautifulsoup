import re
import sys
from bs4 import BeautifulSoup, SoupStrainer

filename = sys.argv[1]

with open(filename, 'r', encoding='utf-8') as file:
    html_doc = file.read()

has_id = SoupStrainer(attrs={'id': True})

soup = BeautifulSoup(html_doc, 'html.parser', parse_only=has_id)

tags_with_id = soup.find_all(True)
for _, tag in enumerate(tags_with_id):
    print(tag)
