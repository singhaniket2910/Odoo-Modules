from odoo import fields, models


class CustomModule(models.Model):
    _name = 'custom.module'
    _description = 'This is just a demo module.'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age', default=1)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Gender', default='other')
