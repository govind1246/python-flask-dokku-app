import datetime
import logging

from flask import request, g

from app import flask
from model.base import HttpResponse
from util.json import json_response


@flask.errorhandler(404)
def not_found(code):
    logging.info("Page not found [%s %s]: %s" % (request.method, request.url, code.code))
    return json_response(HttpResponse(code=code.code, message="Not found")), code.code


@flask.errorhandler(Exception)
def server_error(e):
    code = 500
    logging.error("Internal error [%s %s]: %s" % (request.method, request.url, e))
    logging.exception(e)
    return json_response(HttpResponse(code=code, message="Internal error")), code


@flask.before_request
def before_request():
    g.request_start_time = datetime.datetime.now()
    logging.debug("Before request called for [%s %s]" % (request.method, request.url))



@flask.after_request
def after_request(response):
    logging.debug("After request called for [%s %s: %s" % (request.method, request.url, request.url_rule))
    return response
