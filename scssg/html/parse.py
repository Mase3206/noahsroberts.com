from pathlib import Path
from warnings import warn

import frontmatter
from markdown2 import Markdown

from scssg import (
	GLOBAL_CONF,
	NAV_CONF,
	SLUGS,
)
from scssg.html import (
	PAGES_PATH,
	POSTS_PATH,
	OUTPUT_PATH,
)


PAGES = PAGES_PATH.glob('**/*.md')
POSTS = POSTS_PATH.glob('**/*.md')

md = Markdown()


class Page:
	def __init__(self, path: Path) -> None:
		self.path = path


	@property
	def dest(self) -> Path:
		"""
		The destination path of the page, replicating the folder structure of the source Markdown file.
		"""
		page_path = self.path.relative_to(PAGES_PATH).parent
		return page_path / (self.path.stem + '.html')


	def convert(self):
		with open(self.path, 'r') as f:
			self.meta, content = frontmatter.parse(f.read())
		self.content = md.convert(content)

		return self.meta, self.content
	

	def save_html(self):
		"""Saves the converted HTML to the destination path. THIS DOES NOT USE THE TEMPLATES!"""
		try:
			content = self.content
		except AttributeError:
			self.convert()
			content = self.content
		finally:
			(OUTPUT_PATH / self.dest).parent.mkdir(exist_ok=True, parents=True)
			with open(OUTPUT_PATH / self.dest, 'w+') as f:
				f.write(content)

	

	def match_to_nav(self):
		try:
			keys = self.meta.keys()
		except AttributeError as e:
			self.convert()
			keys = self.meta.keys()
		finally:
			if 'slug' in keys:
				slug = str(self.meta['slug'])
				return SLUGS[slug]


def all_pages():
	"""
	Parse and convert all pages in the PAGES_PATH to HTML files and store them in the OUTPUT_PATH.
	"""

	for pf in PAGES:
		po = Page(pf)
		if not po.match_to_nav():
			warn(f"Discovered page at {pf} is not found in the nav.yml configuration file. This will prevent scssg from automatically linking to the output file.")
		po.save_html()



def _tc():
	# p = Page(PAGES_PATH / Path('hobbies/index.md'))
	# print(p.convert())
	# print(p.match_to_nav())
	# print(p.dest)
	# p.save_html()
	all_pages()

if __name__ == '__main__':
	_tc()
