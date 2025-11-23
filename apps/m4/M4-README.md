# Milestone-4

This update make beautiful soup an iterable object, where users can do
```
// in client space
soup = BeautifulSoup(html_doc, 'html.parser')
for node in soup:
	print(node)
```
The iteration goes in a dfs order and includes all node types like Tag, Comment, and the root node Beautiful soup as well.
