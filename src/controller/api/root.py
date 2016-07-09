from app import flask, controller
from common.conf import Conf
from flask import request
from util.json import dump_json, json_response


@flask.route("/v1/sample/<id>", methods=["GET"])
@controller.api_controller()
def sample_get(id):
    # Sample reding from config
    app_host = Conf.get("app_host")
    return json_response({"id": id, "app_host": app_host})


@flask.route("/v1/sample/<id>", methods=["PUT"])
@controller.api_controller()
def sample_put(id):
    json = request.get_json(force=True)
    if not json:
        json = {}
    json["id"] = id
    return json_response(json)


@flask.route("/v1/sample", methods=["POST"])
@controller.api_controller()
def sample_post():
    json = request.get_json(force=True)
    return json_response(json)


@flask.route("/v1/sample/<id>", methods=["DELETE"])
@controller.api_controller()
def sample_delete(id):
    return json_response({"id": id})


@flask.route('/')
def hello():
    return 'python/flask'
