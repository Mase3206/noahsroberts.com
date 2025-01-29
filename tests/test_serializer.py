from scssg.conf import SerializedObject, yaml_serialize
from pprint import pprint


def test_serializer():
	obj = yaml_serialize('tests/sample.yml')
	pprint(obj)
	