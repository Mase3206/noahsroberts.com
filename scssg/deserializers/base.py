from __future__ import annotations
import yaml
from pathlib import Path
from scssg.helpers import auto_repr
from collections import UserList


class DeserializedObject:
	_class_name = 'DeserializedObject'

	def __init__(self, data: dict):
		for k, v in data.items():
			if type(v) == dict:
				setattr(self, k, DeserializedObject(v))
			elif type(v) == list:
				setattr(self, k, DeserializedList(v))
			else:
				setattr(self, k, v)
	
	def __repr__(self) -> str:
		return auto_repr(self, self._class_name)


class DeserializedList(UserList):
	_class_name = 'DeserializedList'

	def __init__(self, data: list = []):
		self.data = []

		for i in data:
			if type(i) == dict:
				self.data.append(DeserializedObject(i))
			elif type(i) == list:
				self.data.append(DeserializedList(i))
			else:
				self.data.append(i)

	def __repr__(self) -> str:
		data_reprs = []
		for d in self.data:
			data_reprs.append(repr(d))

		return f'[{', '.join(data_reprs)}]'
	

def yaml_deserialize(file_path: Path | str):
	if type(file_path) != Path:
		file_path = Path(file_path)

	with open(file_path, 'r') as f:
		raw = yaml.safe_load(f)

	if type(raw) == dict:
		return DeserializedObject(raw)
	elif type(raw) == list:
		return DeserializedList(raw)
	else:
		raise TypeError('The root element in a Yaml object must be either a list or an object.')
