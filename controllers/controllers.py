# -*- coding: utf-8 -*-
from odoo import http
from num2words import num2words

# class ModuleSomaprec(http.Controller):
#     @http.route('/module_somaprec/module_somaprec/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module_somaprec/module_somaprec/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module_somaprec.listing', {
#             'root': '/module_somaprec/module_somaprec',
#             'objects': http.request.env['module_somaprec.module_somaprec'].search([]),
#         })

#     @http.route('/module_somaprec/module_somaprec/objects/<model("module_somaprec.module_somaprec"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module_somaprec.object', {
#             'object': obj
#         })
