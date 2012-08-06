#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
firebat-manager.test.models
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Objects mapping for blueprint
"""

from sqlalchemy import *
from ..__init__ import db
#from firemanager import db
#from .. import db


class Status(db.Model):
    __tablename__ = 'status'
    id = Column(Integer, primary_key=True)
    name = Column(String(), unique=True)

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return '<Status %r>' % (self.name)


class Test(db.Model):
    __tablename__ = 'test'
    id = Column(Integer, primary_key=True)
    celery_task_id = Column(String)
    status_id = Column(Integer, ForeignKey('status.id'))
    added_at = Column(DateTime)

    def __init__(self, id=None, name=None, status_id=None):
        self.id = id
        self.name = name
        self.status_id = status_id

    def __repr__(self):
        return '<Test %r>' % (self.id)

def init_db():
    db.create_all()
    #statuses = [
    #    Status('added'),
    #    Status('celery_assigned'),
    #    Status('working'),
    #    Status('finishing'),
    #    Status('ended'),
    #    Status('failed'),
    #]

    #for s in statuses:
    #    db.session.add(s)

    #db.session.commit()


if __name__ == '__main__':
    init_db()
