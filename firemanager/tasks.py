# -*- encoding: utf-8 -*-

"""
tankmanager.helpers
~~~~~~~~~~~~~~~~~~~

Common for whole app functions.
"""

from celery import Celery

from firemanager import celeryconfig

celery = Celery()
celery.config_from_object(celeryconfig)

@celery.task
def add(x, y):
        return x + y

@celery.task
def add1(x, y):
    z = 0
    for i in xrange(10 ** 10):
        z = x + y        
    return x + y
