import argparse
from pathlib import Path
import shutil

from scssg.html import render_pages
from scssg.sass import build as build_sass

STATIC_DIR = Path('static')

def build():
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

	build_sass()

	render_pages()

	source = STATIC_DIR
	destination = Path('dist') / STATIC_DIR

	if destination.exists:
		shutil.rmtree(destination)

	shutil.copytree(source, destination)


def launch_server():
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

	parser.add_argument('--serve', action='store_true')

	args = parser.parse_args()


	build()
	if args.serve:
		launch_server()
