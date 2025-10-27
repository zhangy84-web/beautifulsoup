class SoupReplacer(object):
	def __init__(
		self,
		og_tag,
		alt_tag,
	):
		self.og_tag = og_tag
		self.alt_tag = alt_tag

	def replace(self, name):
		if name == self.og_tag:
			return self.alt_tag
		return name