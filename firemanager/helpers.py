# -*- encoding: utf-8 -*-

"""
tankmanager.helpers
~~~~~~~~~~~~~~~~~~~

Common for whole app functions.
"""
import os
from pwd import getpwuid
import commands
import multiprocessing
import collections
from StringIO import StringIO
import logging

import validictory

def owner_by_path(path):
    return getpwuid(os.stat(path).st_uid).pw_name

def get_usage_fire(lock_pth='/var/lock'):
    is_busy = False
    locks = []
    os.chdir(lock_pth)
    for f in os.listdir('.'):
        if f.startswith('lunapark_') and f.endswith('.lock'):
            is_busy = True
            locks.append({
                'file_name': f,
                'created_at': os.path.getmtime(f),
                'owner': owner_by_path(f),
            })
    return {'is_busy': is_busy, 'locks': locks}

def get_usage_cpu():
    result = dict(zip(['1m', '5m', '15m'], os.getloadavg()))
    result['cores_num'] = multiprocessing.cpu_count()
    return result

def get_usage_disk(path='/home', rec=10):
    result = {}
    retcode, du = commands.getstatusoutput(\
    'du -csk %s/* 2>/dev/null | sort -r -n' % path)
    for line in du.split('\n')[:rec + 1]:
        splt = line.split()
        result[splt[1]] = splt[0]
    return result

def get_hops(fqdn):
    retcode, mtr_stdout =commands.getstatusoutput(\
        'mtr --report --report-cycles 1 %s' % str(fqdn))
    
    hops = [h.split()[1] for h in mtr_stdout.split('\n')[1:]]

    result = {
        'hops': hops,
        'hops_num': len(hops)
    }
    return result

def get_logger(dst=None, is_debug=False):
    '''Return logger obj with console hendler.
    '''

    logger = logging.getLogger('fire-manager')
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s  %(message)s')

    hadlers = []
    if  isinstance(dst, basestring):
        hadlers.append(logging.FileHandler(dst))

    if dst and isinstance(dst, StringIO):
        hadlers.append(logging.StreamHandler(com))
    else:
        hadlers.append(logging.StreamHandler())

    if is_debug:
        lvl = logging.DEBUG
    else:
        lvl = logging.INFO

    for h in hadlers:
        h.setLevel(lvl)
        h.setFormatter(formatter)
        logger.addHandler(h)
    return logger
