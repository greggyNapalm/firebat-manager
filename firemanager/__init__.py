#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
firebat-manager.app
~~~~~~~~~~~~~~~~~~~

Describes WSGI application.
"""

import os

import flask
from flask import send_from_directory
from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug.contrib.fixers import ProxyFix

from status import status
from test import test

version_info = (0, 0, 1)
__version__ = ".".join(map(str, version_info))
__path = os.path.dirname(__file__)

app = flask.Flask(__name__)
app.config.from_envvar('FIRE_MNJR_CFG')
app.wsgi_app = ProxyFix(app.wsgi_app)  # Fix for old proxyes
db = SQLAlchemy(app)

# Register different apps
app.register_blueprint(status, url_prefix='/v1/status')
app.register_blueprint(test, url_prefix='/v1/test')


@app.route('/', methods=['GET'])
def index():
    return 'Hello Worlds -->!'


if __name__ == '__main__':
    app.run()
