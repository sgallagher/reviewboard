"""Global configuration for deployment paths and settings.

These values may need to be modified for deployment on different operating
system platforms. Packagers should review this file and patch it appropriately
for their systems.
"""

from __future__ import unicode_literals


#: Location of the sitelist file. This file maintains a list of the installed
#: Review Board sites on this machine and is used when performing a site
#: upgrade to ensure all sites are upgraded together.

SITELIST_FILE_UNIX = "/etc/reviewboard/sites"


#: Default location of the cache directory. This path is used in
#: :command:`rb-site install` if using a file-based cache instead of a
#: memcached-based cache.
DEFAULT_FS_CACHE_PATH = "/var/cache/reviewboard/cache"


#: Preferred location of the Review Board sites. If the :program:`rb-site`
#: tool is passed a site name instead of a full path, it will be prepended
#: with this path.
INSTALLED_SITE_PATH = "/var/lib/reviewboard/sites"

# Username under which the web-server runs
# This will be used to automatically set file ownership appropriately.
# Disabled for upstream, but distro-packagers should set this appropriately.
DEFAULT_WEB_SERVER_USER = "apache"
