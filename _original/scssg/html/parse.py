from pathlib import Path
from warnings import warn

import frontmatter
from markdown2 import Markdown

from scssg import (
	GLOBAL_CONF,
	NAV_CONF,
	SLUGS,
)
from scssg.html.base import (
	PAGES_PATH,
	POSTS_PATH,
	OUTPUT_PATH,
	TEMPLATE_PATH,
)

TEMPLATES = {t.stem: t.relative_to(TEMPLATE_PATH) for t in TEMPLATE_PATH.glob('**/*.html')}
PAGES = PAGES_PATH.glob('**/*.md')
POSTS = POSTS_PATH.glob('**/*.md')

md = Markdown()


class Page:
	def __init__(self, path: Path) -> None:
		self.path = path

		with open(self.path, 'r') as f:
			self.meta, content = frontmatter.parse(f.read())
		self.content = md.convert(content)

		self.title = str(self.meta['title'])
		self.slug = str(self.meta['slug'])
		self.template_name = str(self.meta['template'])


	@property
	def dest(self) -> Path:
		"""
		The destination path of the page, replicating the folder structure of the source Markdown file.
		"""
		page_path = self.path.relative_to(PAGES_PATH).parent
		return page_path / (self.path.stem + '.html')
	

	@property
	def template(self) -> Path:
		"""Return the path to the template as set in the front matter."""
		if (template := TEMPLATES.get(self.template_name, None)):
			return template
		else:
			raise FileNotFoundError(f'Template {self.template_name}.html for type {self.template_name} not found in the templates directory {TEMPLATE_PATH}')
	

	def save_html(self):
		"""Saves the converted HTML to the destination path. THIS DOES NOT USE THE TEMPLATES!"""
		
		(OUTPUT_PATH / self.dest).parent.mkdir(exist_ok=True, parents=True)
		with open(OUTPUT_PATH / self.dest, 'w+') as f:
			f.write(self.content)

	

	
	def match_to_nav(self):
		if 'slug' in self.meta.keys():
			slug = str(self.meta['slug'])
			return SLUGS.get(slug, None)



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
	p = Page(PAGES_PATH / Path('resume.md'))
	print(p.match_to_nav())
	print(p.dest)
	print(p.template)

if __name__ == '__main__':
	_tc()
