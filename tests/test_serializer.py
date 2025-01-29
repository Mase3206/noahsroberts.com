from scssg.conf import SerializedObject, yaml_serialize


def test_serializer():
	obj = yaml_serialize('tests/sample.yml')
	