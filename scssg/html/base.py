from pathlib import Path

from jinja2 import Environment, PackageLoader, select_autoescape

PAGES_PATH = Path('pages')
POSTS_PATH = Path('posts')
OUTPUT_PATH = Path('dist')
TEMPLATE_PATH = Path('templates')


env = Environment(
    # loader=FileSystemLoader("templates"),
	loader=PackageLoader('scssg', str(TEMPLATE_PATH.resolve())),
    autoescape=select_autoescape()
)