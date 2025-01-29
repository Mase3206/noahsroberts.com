from scssg.deserializers.global_conf import GlobalConfiguration
from scssg.deserializers.nav import NavLinks


GLOBAL_CONF = GlobalConfiguration.deserialize('config/global.yml')
NAV_CONF = NavLinks.deserialize('config/nav.yml')


__all__ = [
	'GLOBAL_CONF',
	'NAV_CONF'
]