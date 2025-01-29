from __future__ import annotations
import yaml
from pathlib import Path
from scssg.helpers import auto_repr
from collections import UserList


class SerializedObject:
	_class_name = 'SerializedObject'

	def __init__(self, data: dict):
		for k, v in data.items():
			if type(v) == dict:
				setattr(self, k, SerializedObject(v))
			elif type(v) == list:
				setattr(self, k, SerializedList(v))
			else:
				setattr(self, k, v)
	
	def __repr__(self) -> str:
		return auto_repr(self, self._class_name)


class SerializedList(UserList):
	_class_name = 'SerializedList'

	def __init__(self, data: list = []):
		self.data = []

		for i in data:
			if type(i) == dict:
				self.data.append(SerializedObject(i))
			elif type(i) == list:
				self.data.append(SerializedList(i))
			else:
				self.data.append(i)

	def __repr__(self) -> str:
		data_reprs = []
		for d in self.data:
			data_reprs.append(repr(d))

		return f'[{', '.join(data_reprs)}]'
	

def convert_serialized_list_to_list(lst: SerializedList) -> list:
	return list(lst.data)


def yaml_serialize(file_path: Path | str):
	if type(file_path) != Path:
		file_path = Path(file_path)

	with open(file_path, 'r') as f:
		raw = yaml.safe_load(f)

	if type(raw) == dict:
		return SerializedObject(raw)
	elif type(raw) == list:
		return SerializedList(raw)
	else:
		raise TypeError('The root element in a Yaml object must be either a list or an object.')



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
