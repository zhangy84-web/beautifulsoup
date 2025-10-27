import sys
from bs4 import BeautifulSoup, SoupReplacer

filename = sys.argv[1]

with open(filename, 'r', encoding='utf-8') as file:
    html_doc = file.read()

replacer = SoupReplacer('b', 'blockquote')

soup = BeautifulSoup(html_doc, 'html.parser', replacer=replacer)

with open("blockquote_" + filename, 'w', encoding='utf-8') as outfile:
	outfile.write(soup.prettify())
