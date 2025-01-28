def build():
	"""
	Run a full build of the entire site.

	Steps
	-----
	1. Compile HTML from templates
		1. Convert Markdown to HTML
		2. Insert converted Markdown into templates
		3. Resolve `base` and `include` template tags
	2. Build Preact elements
	3. Build Sass styling
	"""
