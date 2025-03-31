import subprocess


def build(minified = True):
	if minified:
		subprocess.run(
			['sass', '--style=compressed', '--source-map', 'static/sass/style.sass', 'static/css/style.css']
		)
	else:
		subprocess.run(
			['sass', '--style=expanded', '--source-map', 'static/sass/style.sass', 'static/css/style.css']
		)
