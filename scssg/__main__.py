import subprocess

def build():
	"""
	Build the site.

	Full build steps
	----------------
	1. Compile HTML from templates
		1. Convert Markdown to HTML
		2. Insert converted Markdown into templates
		3. Resolve `base` and `include` template tags
	2. Build Sass styling
	"""
