import os

from flask import Flask

from common.conf import Conf
# from common.context import Context
from common.decorator import Controller, Permissions, Security

flask = Flask(__name__, template_folder="templates", static_folder="../static")
Conf.get_instance().init(os.path.dirname(os.path.realpath(__file__)))
# Context.get_instance().init()

controller = Controller.get_instance()
permissions = Permissions.get_instance()
security = Security.get_instance()
