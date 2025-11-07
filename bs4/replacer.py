class SoupReplacer(object):
	"""
	A  class to replace attributes while parsing the tree.
	"""
	def __init__(
		self,
		og_tag=None,
		alt_tag=None,
		name_xformer=None,
		attrs_xformer=None,
		xformer=None,
	):
		self.og_tag = og_tag
		self.alt_tag = alt_tag
		self.name_xformer = name_xformer
		self.attrs_xformer = attrs_xformer
		self.xformer = xformer

	def replace_name(self, name):
		"""
		Replace the name, using og_tag, alt_tag, and name_xformer.

		Args:
            name (str): name of the tag
            
        Returns:
        	new_name
        """
		if self.og_tag and self.alt_tag:
			if name == self.og_tag:
				return self.alt_tag
		return name

	def replace_tag(self, tag):
		"""
		Replace the tag.

		Args:
            tag (Tag): tag that needs to be xtransformed
            
        Returns:
            new_name, new_attrs (tuple)
        """
		if not tag:
			return
		if self.name_xformer:
			tag.name = self.name_xformer(tag)
		if self.attrs_xformer:
			tag.attrs = self.attrs_xformer(tag)
		if self.xformer:
			self.xformer(tag)
