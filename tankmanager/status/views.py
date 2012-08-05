# -*- encoding: utf-8 -*-

"""
tankmanager.status
~~~~~~~~~~~~~~~~~~

Get tanks current status:
    * test lock file
    * file system usage
    * logged users
    * etc
"""
import os
from pwd import getpwuid
import commands
import multiprocessing
import collections

from flask import request, jsonify, url_for, abort, redirect, flash

from . import status
from .. helpers import get_usage_fire

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

@status.route('/usage/<tgt>', methods=['GET'])
def usage(tgt):
    if str(tgt) == 'all':
        result = {
            'cpu': get_usage_cpu(),
            'disk': get_usage_disk(),
            'fire': get_usage_fire(),
        }
        return jsonify(result)

    if str(tgt) == 'cpu':
        return jsonify(get_usage_cpu()) 

    if str(tgt) == 'disk':
        return jsonify(get_usage_disk()) 

    if str(tgt) == 'fire':
        return jsonify(get_usage_fire())

    return 'No such tgt', 404 
