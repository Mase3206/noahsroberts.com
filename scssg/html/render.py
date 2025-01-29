from jinja2 import meta
from pathlib import Path

from scssg import (
	global_conf,
	nav
)
from scssg.html import env


class TestPageConf:
	title = "Test"
	slug = 'test'
	source = 'test.md'


def render_to_html(template: Path, page: TestPageConf, output_path: Path):
	t = env.get_template(str(template))
	r = t.render(
		nav_items = nav,
		global_conf = global_conf,
		page = page,
	)
	with open(output_path / template.parent / (page.slug + '.html'), 'w+') as out:
		out.write(r)

	return r



def _tc():
	out = render_to_html(
		Path('base.html'),
		TestPageConf(),
		Path('dist')
	)
	print(out)


if __name__ == '__main__':
	_tc()
