# -*- encoding: utf-8 -*-

"""
tankmanager.test
~~~~~~~~~~~~~~~~

Launch tests, get their detailt.
"""

from flask import request, jsonify, url_for, abort, redirect, flash

import validictory
from firebat.console.helpers import validate as fb_validate

from . import test
from .models import Status, Test 
from .. helpers import get_usage_fire
from .. tasks import add, add1


@test.route('/luna/<id>', methods=['GET'])
def luna_info(id):
    for lock in get_usage_fire()['locks']:
        if str(id) in lock['file_name']:
            return jsonify(lock)
    return 'No suck fire', 404


@test.route('/firebat', methods=['POST'])
def firebat():
    test = request.json
    if not test:
        return 'JSON body malformed', 400

    try:
        fb_validate(test)
    except validictory.validator.ValidationError, e:
        return 'Test schema malformed: %s' % e, 400

    task = add.delay(4, 4)
    return task.id

@test.route('/firebat/<task_id>', methods=['GET'])
def firebat_c(task_id):
    '''Get firebat test state by id'''
    r = add.AsyncResult(task_id)

    result = {
        'ready': r.ready()
    }

    if r.ready():
        result['result'] = r.get(timeout=5)

    return jsonify(result)
