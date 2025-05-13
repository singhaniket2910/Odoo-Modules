from odoo import fields, models


class CustomModule(models.Model):
    _name = 'custom.module'
    _description = 'This is just a demo module.'

    name1 = fields.Char('Name1', required=True)
    name2 = fields.Char('Name2', required=True)
    name3 = fields.Char('Name3', required=True)
    name4 = fields.Char('Name4', required=True)
    name5 = fields.Char('Name5', required=True)
