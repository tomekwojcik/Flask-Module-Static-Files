# -*- coding: utf-8 -*-
from flask import Flask

class app_config(object):
    DEBUG = True

def make_app():
    app = Flask(__name__)

    from admin import admin
    from frontend import frontend
    
    config = app_config()
    app.config.from_object(config)

    app.register_module(frontend)
    app.register_module(admin)

    return app
