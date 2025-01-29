from __future__ import annotations
from pathlib import Path
import yaml

from scssg.serializers.base import SerializedList, SerializedObject


class StyleConf(SerializedObject):
	classes: list[str]
	_class_name = 'StyleConf'

	def __init__(self, data: dict):
		for k, v in data.items():
			if type(v) == dict:
				setattr(self, k, SerializedObject(v))
			elif type(v) == list:
				setattr(self, k, SerializedList(v))
			else:
				setattr(self, k, v)


class NavLinkConf(SerializedObject):
	name: str
	slug: str
	style: StyleConf
	contains: NavLinks
	_class_name = 'NavLinkConf'

	def __init__(self, data: dict):
		for k, v in data.items():
			if type(v) == dict:
				if k == 'style':
					setattr(self, k, StyleConf(v))
				else:
					setattr(self, k, SerializedObject(v))
			elif type(v) == list:
				if k == 'contains':
					setattr(self, k, NavLinks(v))
				else:
					setattr(self, k, SerializedList(v))
			else:
				setattr(self, k, v)



class NavLinks(SerializedList):
	data: list[NavLinkConf]
	_class_name = 'NavLinks'

	def __init__(self, data: list = []):
		self.data = []

		for i in data:
			if type(i) == dict:
				self.data.append(NavLinkConf(i))
			else:
				raise TypeError('The root element in nav.yml must contain a list of objects.')
	

	@staticmethod
	def serialize(file_path: Path | str):
		if type(file_path) != Path:
			file_path = Path(file_path)

		with open(file_path, 'r') as f:
			raw = yaml.safe_load(f)

		if type(raw) == list:
			return NavLinks(raw)
		else:
			raise TypeError(f'The root element in nav.yml must be a list. Found type {type(raw)}')
		
	def __getitem__(self, index: int) -> NavLinkConf:
		return self.data[index]
	
	def __repr__(self) -> str:
		data_reprs = []
		for d in self.data:
			data_reprs.append(repr(d))

		return f'{self._class_name}([{', '.join(data_reprs)}])'



def _tc():
	obj = NavLinks.serialize('tests/sample.yml')
	print(obj)


if __name__ == '__main__':
	_tc()
