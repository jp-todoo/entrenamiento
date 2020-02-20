# -*- coding: utf-8 -*-

from odoo import models, fields


class entrenamiento1(models.Model):
     _name = 'entrenamiento1.entrenamiento1'
     _description = 'entrenamiento1.entrenamiento1'

     Nombre = fields.Char()
     Valor = fields.Integer()
     Tipo= fields.Float(compute="_value_pc", store=True)
     Observación = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
