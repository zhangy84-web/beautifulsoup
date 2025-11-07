import sys
from bs4 import BeautifulSoup, SoupReplacer

filename = sys.argv[1]

with open(filename, 'r', encoding='utf-8') as file:
    html_doc = file.read()

def replace_p_tags(tag):
	if tag.name == "p":
		tag.attrs["class"] = "test"

replacer = SoupReplacer(xformer=replace_p_tags)

soup = BeautifulSoup(html_doc, 'html.parser', replacer=replacer)

with open("task7_" + filename, 'w', encoding='utf-8') as outfile:
	outfile.write(soup.prettify())