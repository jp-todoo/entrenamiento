# -*- coding: utf-8 -*-
# from odoo import http


# class Entrenamiento(http.Controller):
#     @http.route('/entrenamiento/entrenamiento/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/entrenamiento/entrenamiento/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('entrenamiento.listing', {
#             'root': '/entrenamiento/entrenamiento',
#             'objects': http.request.env['entrenamiento.entrenamiento'].search([]),
#         })

#     @http.route('/entrenamiento/entrenamiento/objects/<model("entrenamiento.entrenamiento"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('entrenamiento.object', {
#             'object': obj
#         })
