Plone hosting buildout
======================

Process control
---------------

All services are controlled using the supervisord_ process manager. Supervisord
takes care of starting all daemons, restarting them when needed and can
optionally provide a web interface allowing for easy remote management.

To start supervisord starts its daemon ``bin/supervisord``. This will
automatically start the ZEO server, Zope and, if enabled, Varnish. You
start, stop and restart those via the ``bin/supervisorctl`` utility.

To start all processes automatically on system boot it is necessary to
start supervisord as part of the system boot process. This can easily
be done by adding a crontab entry to the account used for your site::

  # Automatically start the plone.org website
  @reboot /srv/plone.org/bin/supervisord -c /srv/plone.org/etc/supervisord.conf

.. _supervisord: http://www.supervisord.org/


Log rotation
------------

This buildout includes a configuration for ``logrotate``, which is included
in all common Linux distributions. To setup log rotation you will need to
add an entry to the crontab entry for the account user for your site::

  # Rotate plone.org logfiles at 06:00
  0 6 * * * /usr/sbin/logrotate --state /srv/plone.org/var/logrotate.status /srv/plone.org/etc/logrotate.conf


Selecting product and package versions
--------------------------------------

For production environment it is generally a good idea to enforce
use of specific, tested, versions of all packages and products. This
can prevent unexpected surprises when updating a buildout environment
or deploying it on another machine.

For Zope2 products it is recommended to use a release tar or zip-archive.
This can be installed using the *productdistros* section in ``buildout.cfg``.
See `plone.recipe.distros`_ for more information.

Packages can be pinned down in the *versions* section, also located in
``buildout.cfg``.

.. _plone.recipe.distros: http://pypi.python.org/pypi/plone.recipe.distros

