from scssg.deserializers.global_conf import GlobalConfiguration
from scssg.deserializers.nav import NavLinks


global_conf = GlobalConfiguration.deserialize('config/global.yml')
nav = NavLinks.deserialize('config/nav.yml')


__all__ = [
	'global_conf',
	'nav'
]