import argparse
from pathlib import Path
import shutil

from scssg.html import render_pages
from scssg.sass import build as build_sass

STATIC_DIR = Path('static')

def build(args: argparse.Namespace):
	"""
	Build the site.

	Full build steps
	----------------
	1. Build Sass styling
	2. Compile HTML from templates
		1. Convert Markdown to HTML
		2. Insert converted Markdown into templates
		3. Resolve `base` and `include` template tags
	"""

	print('Building CSS stylesheet from Sass source')
	build_sass()

	print('Copying built CSS stylesheet to dist folder')
	source = STATIC_DIR
	destination = Path('dist') / STATIC_DIR

	if destination.exists:
		shutil.rmtree(destination)

	shutil.copytree(source, destination)

	print('Rendering Markdown pages to HTML and saving to dist folder')
	render_pages()


def serve(args: argparse.Namespace):
	from http.server import HTTPServer, SimpleHTTPRequestHandler

	class Handler(SimpleHTTPRequestHandler):
		def __init__(self, *args, **kwargs):
			super().__init__(*args, directory='dist', **kwargs)
	
	with HTTPServer(
		server_address = ('', 8000),
		RequestHandlerClass = Handler,
	) as httpd:
		print('\nNow serving at http://localhost:8000')
		try:
			httpd.serve_forever()
		except KeyboardInterrupt:
			print('\nStopping dev server...')
			exit(0)
		



def cli():
	parser = argparse.ArgumentParser()
	parser.set_defaults(func=lambda args: (parser.print_usage(), exit(1)))

	sp = parser.add_subparsers()

	sp_serve = sp.add_parser('serve')
	# sp_serve.add_argument('--watch', action='store_true')
	sp_serve.set_defaults(func=lambda args: (build(args), serve(args)))

	sp_build = sp.add_parser('build')
	sp_build.set_defaults(func=build)

	args = parser.parse_args()

	args.func(args)
