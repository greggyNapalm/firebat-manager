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
from .. helpers import get_usage_fire


@test.route('/luna/<id>', methods=['GET'])
def luna_info(id):
    for lock in get_usage_fire()['locks']:
        if str(id) in lock['file_name']:
            return jsonify(lock)
    return 'No suck fire', 404


@test.route('/firebat/<id>', methods=['POST'])
def firebat(id):
    #if int(id) == -1:  # No global fire ID, shud use temporary instead.
    #    return 'I\'ll make local ID, than'
    test = request.json
    if not test:
        return 'JSON body malformed', 400

    try:
        fb_validate(test)
    except validictory.validator.ValidationError, e:
        return 'Test schema malformed: %s' % e, 400

    return 'No suck fire'
