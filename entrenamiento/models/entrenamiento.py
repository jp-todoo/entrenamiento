# -*- coding: utf-8 -*-

from odoo import models, fields


class entrenamiento(models.Model):
     _name = 'entrenamiento.entrenamiento'
     _description = 'entrenamiento.entrenamiento'

     Nombre = fields.Char()
     Valor = fields.Integer()
     Tipo= fields.Float(compute="_value_pc", store=True)
     Observacion = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
