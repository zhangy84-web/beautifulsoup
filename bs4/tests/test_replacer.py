from bs4 import BeautifulSoup, SoupReplacer

class TestReplacer:
	def test_replace_tag(self):
		html_doc = """
		<body>
		<og></og>
		<not_og></not_og>
		</body>
		"""
		replacer = SoupReplacer("og", "alt")
		soup = BeautifulSoup(html_doc, "html.parser", replacer=replacer)

		# Target tag is replaced
		assert soup.find("og") is None
		assert soup.find("alt") is not None

		# None target tag is not replaced
		assert soup.find("not_og") is not None

	def test_replace_closed_tag(self):
		html_doc = """
		<body>
		<og>
		<not_og>
		</body>
		"""
		replacer = SoupReplacer("og", "alt")
		soup = BeautifulSoup(html_doc, "html.parser", replacer=replacer)

		# Target tag is replaced
		assert soup.find("og") is None
		assert soup.find("alt") is not None

		# None target tag is not replaced
		assert soup.find("not_og") is not None
