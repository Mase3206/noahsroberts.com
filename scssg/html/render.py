from jinja2 import meta
from pathlib import Path

from scssg import (
	GLOBAL_CONF,
	NAV_CONF
)
from scssg.html import (
	env,
	OUTPUT_PATH
)


class TestPageConf:
	title = "Test"
	slug = 'test'
	source = 'test.md'


def render_to_html(template: Path, page: TestPageConf):
	t = env.get_template(str(template))
	r = t.render(
		nav_items = NAV_CONF,
		global_conf = GLOBAL_CONF,
		page = page,
	)
	with open(OUTPUT_PATH / template.parent / (page.slug + '.html'), 'w+') as out:
		out.write(r)

	return r



def _tc():
	out = render_to_html(
		Path('base.html'),
		TestPageConf(),
	)
	print(out)


if __name__ == '__main__':
	_tc()
