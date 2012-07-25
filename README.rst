Firebat-Manager
===============

Netwrok application with manages test tasks on one load generation host and acts
as a data relay.

Documentation
-------------

Coming soon

Requirements
------------

* GNU Linux
* Python >= 2.7 (Not Python3)

Installation
------------

Use pip and `vurtualev/virtualenvwrapper <http://docs.python-guide.org/en/latest/dev/virtualenvs/>`_

Stable version:

::

    Coming soon

Development version:

::

    $ git clone git://github.com/greggyNapalm/firebat-manager.git; cd firebat-manager
    $ pip install -r requirements-dev.txt
    $ cp -p firebat-manager.default.cfg firebat-manager.local.cfg
    $ export FIRE_MNG_CFG=`readlink -e firebat-web.local.cfg`
    $ ./run.py


Screenshots
-----------

Coming soon

Issues
------

Find a bug? Want a feature? Submit an `here <https://github.com/greggyNapalm/firebat-manager/issues>`_. Patches welcome!

License
-------
BSD `Read more <http://opensource.org/licenses/BSD-3-Clause>`_
