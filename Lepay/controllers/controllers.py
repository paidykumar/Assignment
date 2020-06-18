# -*- coding: utf-8 -*-
from odoo import http, fields
from odoo.http import request


class lepay_controller(http.Controller):

    @http.route('/lepay', website=True, auth='public')
    def index(self, **kw):
        return "hello"
