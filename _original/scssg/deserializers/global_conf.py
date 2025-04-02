from __future__ import annotations
from pathlib import Path
import yaml

from scssg.deserializers.base import DeserializedList, DeserializedObject


class GlobalConfiguration(DeserializedObject):
	title: str
	_class_name = 'GlobalConfiguration'

	@staticmethod
	def deserialize(file_path: Path | str):
		if type(file_path) != Path:
			file_path = Path(file_path)

		with open(file_path, 'r') as f:
			raw = yaml.safe_load(f)

		if type(raw) == dict:
			return GlobalConfiguration(raw)
		else:
			raise TypeError(f'The root element in global.yml must be an object. Found type {type(raw)}')
		

def _tc():
	obj = GlobalConfiguration.deserialize('config/global.yml')
	print(obj)

if __name__ == '__main__':
	_tc()
