from __future__ import annotations
from pathlib import Path
import yaml

from scssg.deserializers.base import DeserializedList, DeserializedObject


def prefix_slug_to_url(prefix: str, slug: str):
	if prefix == '':
		return slug
	elif prefix == '/':
		return f'/{slug}'
	else:
		return f'{prefix}/{slug}'
	

class StyleConf(DeserializedObject):
	classes: list[str]
	_class_name = 'StyleConf'

	def __init__(self, data: dict):
		for k, v in data.items():
			if type(v) == dict:
				setattr(self, k, DeserializedObject(v))
			elif type(v) == list:
				setattr(self, k, DeserializedList(v))
			else:
				setattr(self, k, v)

	@property
	def html_classes(self):
		return ' '.join(self.classes)


class NavLinkConf(DeserializedObject):
	name: str
	slug: str
	style: StyleConf
	contains: NavLinks
	hidden: bool
	has_children: bool
	prefix: str
	_class_name = 'NavLinkConf'

	def __init__(self, data: dict, prefix: str = ''):
		self.prefix = prefix
		self.has_children = False
		
		for k, v in data.items():
			if type(v) == dict:
				if k == 'style':
					setattr(self, k, StyleConf(v))
				else:
					setattr(self, k, DeserializedObject(v))
				
			elif type(v) == list:
				# self.prefix = prefix
				if k == 'contains':
					self.has_children = True
					pref = prefix_slug_to_url(self.prefix, self.slug)
					setattr(self, k, NavLinks(v, prefix=pref))
				
				else:
					setattr(self, k, DeserializedList(v))
			
			else:
				setattr(self, k, v)

		try:
			_ = self.hidden
		except AttributeError:
			self.hidden = False


	def set_prefix(self, slug: str):
		# try:
		self.prefix = f'{self.prefix}/{slug}'
		# except AttributeError:
		# 	self.prefix = slug

	@property
	def url(self) -> str:
		# return f'{self.prefix}/{self.slug}' if self.prefix != ('' or '/') else self.slug
		return prefix_slug_to_url(self.prefix, self.slug)
	


class NavLinks(DeserializedList):
	data: list[NavLinkConf]
	_class_name = 'NavLinks'
	# parent: NavLinkConf

	def __init__(
		self, 
		data: list = [],
		prefix: str = '',
	):
		self.data = []

		for i in data:
			if type(i) == dict:
				self.data.append(NavLinkConf(i, prefix=prefix))
			else:
				raise TypeError('The root element in nav.yml must contain a list of objects.')
	

	@staticmethod
	def deserialize(file_path: Path | str):
		if type(file_path) != Path:
			file_path = Path(file_path)

		with open(file_path, 'r') as f:
			raw = yaml.safe_load(f)

		if type(raw) == list:
			return NavLinks(raw, prefix='/')
		else:
			raise TypeError(f'The root element in nav.yml must be a list. Found type {type(raw)}')
		
	def __getitem__(self, index: int) -> NavLinkConf:
		return self.data[index]
	
	def __repr__(self) -> str:
		data_reprs = []
		for d in self.data:
			data_reprs.append(repr(d))

		return f'{self._class_name}([{', '.join(data_reprs)}])'



def collect_slugs(nav_conf: NavLinks) -> dict[str, NavLinkConf]:
	slugs: dict[str, NavLinkConf] = {}
	for l in nav_conf:
		slugs[l.slug] = l

		if l.has_children:
			s = collect_slugs(l.contains)
			for k, v in s.items():
				slugs[k] = v
	
	return slugs



def _tc():
	from pprint import pprint
	obj = NavLinks.deserialize('config/nav.yml')
	pprint(obj)


if __name__ == '__main__':
	_tc()
