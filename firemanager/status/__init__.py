# -*- encoding: utf-8 -*-
import flask

status = flask.Blueprint('status', __name__)

from . import views
