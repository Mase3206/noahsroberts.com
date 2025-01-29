import yaml
from pathlib import Path


class SerializedObject:
	def __init__(self, data: dict):
		for k, v in data:
			if type(v) == dict:
				setattr(self, k, SerializedObject(v))


def yaml_serialize(file_path: Path | str) -> SerializedObject:
	if type(file_path) != Path:
		file_path = Path(file_path)
		
	with open(file_path, 'r') as f:
		raw = yaml.safe_load(f)

	return SerializedObject(raw)
