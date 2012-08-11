#!/usr/bin/env python

"""
firebat-manager.populate_db
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Command line script to create sqlite db file with schema.
**For initial deployment only**
"""

from firemanager import db
from firemanager.test.models import Status, Test 


def main():
    db.create_all()
    statuses = [
        Status('added'),
        Status('celery_assigned'),
        Status('working'),
        Status('finishing'),
        Status('ended'),
        Status('failed'),
    ]

    for s in statuses:
        db.session.add(s)

    db.session.commit()

if __name__ == '__main__':
    main()
