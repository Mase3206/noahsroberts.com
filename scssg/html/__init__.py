from pathlib import Path

from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader

env = Environment(
    # loader=FileSystemLoader("templates"),
	loader=PackageLoader('scssg', '../templates'),
    autoescape=select_autoescape()
)

PAGES_PATH = Path('pages')
POSTS_PATH = Path('posts')
OUTPUT_PATH = Path('dist')