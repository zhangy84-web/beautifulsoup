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

	def test_replace_name_xformer(self):
		html_doc = """
		<body>
		<b>nameIsB</b>
		<p>notB</p>
		</body>
		"""
		replacer = SoupReplacer(name_xformer=lambda tag: "blockquote" if tag.name == "b" else tag.name)
		soup = BeautifulSoup(html_doc, "html.parser", replacer=replacer)

		# Replace <b> using name_xformer
		assert soup.find("b") is None
		assert soup.find("blockquote") is not None
		# No replace for other tags
		assert soup.find("p") is not None

	def test_replace_name_xformer_upper(self):
		html_doc = """
		<body>
		<b>nameIsB</b>
		<p>notB</p>
		</body>
		"""
		def make_upper(tag):
			return tag.name.upper()
		replacer = SoupReplacer(name_xformer=make_upper)
		soup = BeautifulSoup(html_doc, "html.parser", replacer=replacer)

		assert soup.find("b") is None
		assert soup.find("B") is not None
		assert soup.find("p") is None
		assert soup.find("P") is not None

	def test_replace_attrs_xformer(self):
		html_doc = """
		<body>
		<b class="something"></b>
		</body>
		"""
		def remove_class_attr(tag):
			if "class" in tag.attrs:
				del tag.attrs["class"]
				return tag.attrs
		replacer = SoupReplacer(attrs_xformer=remove_class_attr)
		soup = BeautifulSoup(html_doc, "html.parser", replacer=replacer)

		assert soup.find("b") is not None
		assert "class" not in soup.find("b")

	def test_replace_attrs_xformer_replace(self):
		html_doc = """
		<body>
		<b class="something"></b>
		</body>
		"""
		def change_class_attr(tag):
			if "class" in tag.attrs:
				tag.attrs["class"] = "other"
			return tag.attrs
		replacer = SoupReplacer(attrs_xformer=change_class_attr)
		soup = BeautifulSoup(html_doc, "html.parser", replacer=replacer)

		assert soup.find("b") is not None
		assert "other" in soup.find("b").get("class", [])

	def test_replace_xformer(self):
		html_doc = """
		<body>
		<b class="something"></b>
		</body>
		"""
		def remove_class_attr(tag):
			if "class" in tag.attrs:
				del tag.attrs["class"]
		replacer = SoupReplacer(xformer=remove_class_attr)
		soup = BeautifulSoup(html_doc, "html.parser", replacer=replacer)

		assert soup.find("b") is not None
		assert "class" not in soup.find("b")

	def test_replace_xformer(self):
		html_doc = """
		<b></b>
		"""
		def add_class_attr(tag):
			if "class" not in tag.attrs:
				tag.attrs["class"] = "test"
		replacer = SoupReplacer(xformer=add_class_attr)
		soup = BeautifulSoup(html_doc, "html.parser", replacer=replacer)

		assert soup.find("b") is not None
		assert "test" in soup.find("b").get("class", [])
