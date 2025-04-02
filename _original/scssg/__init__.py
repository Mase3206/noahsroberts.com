from scssg.deserializers.global_conf import GlobalConfiguration
from scssg.deserializers.nav import NavLinks, collect_slugs

GLOBAL_CONF = GlobalConfiguration.deserialize('config/global.yml')
NAV_CONF = NavLinks.deserialize('config/nav.yml')
SLUGS = collect_slugs(NAV_CONF)


__all__ = [
	'GLOBAL_CONF',
	'NAV_CONF',
	'SLUGS',
]