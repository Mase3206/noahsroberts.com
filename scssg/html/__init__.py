from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader

env = Environment(
    # loader=FileSystemLoader("templates"),
	loader=PackageLoader('scssg', '../templates'),
    autoescape=select_autoescape()
)