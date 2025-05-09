# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class /mnt/extra-addons/custom_module(models.Model):
#     _name = '/mnt/extra-addons/custom_module./mnt/extra-addons/custom_module'
#     _description = '/mnt/extra-addons/custom_module./mnt/extra-addons/custom_module'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

from odoo import fields, models, api


class CustomModel(models.Model):
    _name = 'custom.model'
    _description = 'Custom Model'

    name = fields.Char(string='Name', required=True)
    description = fields.Char(string='Description')
