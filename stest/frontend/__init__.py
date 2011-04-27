# -*- coding: utf-8 -*-

from flask import Module, render_template

frontend = Module(__name__)

@frontend.route('/')
def frontend_index():
    return render_template('frontend/index.html')
