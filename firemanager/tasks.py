# -*- encoding: utf-8 -*-

"""
tankmanager.helpers
~~~~~~~~~~~~~~~~~~~

Common for whole app functions.
"""

import os
#from datetime import datetime
import time
import logging

import validictory
from celery import Celery
from celery.contrib import rdb
from firebat.console.helpers import validate, get_logger
from firebat.console.proc import get_ammo, build_test, start_daemon
from firebat.console.exceptions import FireEmergencyExit

from firemanager import celeryconfig


class StrLogger(object):
    def __init__(self):
        self.msgs = {}
        self.handlers = True

    def add_msg(self, msg, lvl):
        self.msgs[int(time.time())] = {
            'msg': msg,
            'lvl': lvl,
        }

    def debug(self, msg):
        self.add_msg(msg, 'debug')
        
    def info(self, msg):
        self.add_msg(msg, 'info')
 
    def warn(self, msg):
        self.add_msg(msg, 'warn')
        
    def error(self, msg):
        self.add_msg(msg, 'error')

    def critical(self, msg):
        self.add_msg(msg, 'critical')

def get_robo_logger(logs_path, test_id, is_debug=False):
    '''Return logger obj with file hendler.
    '''
    logger = logging.getLogger('root')
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s ' + 'test:%s' % test_id + ' %(message)s')

    log_path = '%s/test_%s.log' % (logs_path, test_id)
    hadlers = []
    hadlers.append(logging.FileHandler(log_path))

    if is_debug:
        lvl = logging.DEBUG
    else:
        lvl = logging.INFO

    for h in hadlers:
        h.setLevel(lvl)
        h.setFormatter(formatter)
        logger.addHandler(h)
    return logger

celery = Celery()
celery.config_from_object(celeryconfig)

@celery.task
def add(x, y):
        #'a' + 4
        #assert False
        return x + y

@celery.task
def add1(x, y):
    z = 0
    for i in xrange(10 ** 10):
        z = x + y        
    return x + y

@celery.task
def launch_fire(test_id, test_cfg, base_path, armorer_api_url=None,
                logs_path='/tmp'):
    logger = get_robo_logger(logs_path, test_id, is_debug=False)

    #wd = '%s/%s' % (base_path, test_id)
    if not os.path.exists(base_path):
        os.makedirs(base_path)
    os.chdir(base_path)

    try:
        validate(test_cfg)
    except validictory.validator.ValidationError, e:
        return 1, 'Error in parsing fire conf:\n%s' % e

    if 'ammo' in test_cfg:
        test_cfg = get_ammo(test_cfg)

    try:
        build_test(test_cfg)
    except FireEmergencyExit, e:
        return 1, str(e)

    for f in test_cfg['fire']:
        retcode, out = start_daemon(f)
        if retcode == 0:
            logger.info('Fire %s launched successfully.' % f['name'])
        else:
            logger.error('Fire start fails: %s.Exit code: %s' % (out, retcode))
    return 0, 'Supervisors launched successfully.' 
