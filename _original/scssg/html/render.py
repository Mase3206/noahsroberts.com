from warnings import warn
from pathlib import Path

from scssg import (
	GLOBAL_CONF,
	NAV_CONF
)
from scssg.html.base import (
	env,
	PAGES_PATH,
	POSTS_PATH,
	OUTPUT_PATH,
	TEMPLATE_PATH,
)
from scssg.html.parse import Page



TEMPLATES = {t.stem: t.relative_to(TEMPLATE_PATH) for t in TEMPLATE_PATH.glob('**/*.html')}
PAGES = PAGES_PATH.glob('**/*.md')
POSTS = POSTS_PATH.glob('**/*.md')


class TestPageConf:
	title = "Test"
	slug = 'test'
	source = 'test.md'


def render_single_page(page: Page):
	template = env.get_template(str(page.template))
	rendered = template.render(
		nav_items = NAV_CONF,
		global_conf = GLOBAL_CONF,
		page = page,
	)

	outpath = OUTPUT_PATH / page.dest
	outpath.parent.mkdir(exist_ok=True, parents=True)
	with open(outpath, 'w+') as out:
		out.write(rendered)

	return rendered


def render_pages():
	for pf in PAGES:
		po = Page(pf)
		if not po.match_to_nav():
			warn(f"Discovered page at {pf} is not found in the nav.yml configuration file. This will prevent scssg from automatically linking to the output file.")
		render_single_page(po)


def _tc():
	out = render_single_page(Page(PAGES_PATH / Path('resume.md')),)
	print(out)


if __name__ == '__main__':
	_tc()
