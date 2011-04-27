# -*- coding: utf-8 -*-

from flask import Module, render_template

admin = Module(__name__, url_prefix='/admin')

@admin.route('/')
def admin_index():
    return render_template('admin/index.html')
