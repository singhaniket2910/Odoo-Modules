from odoo import models, fields


class Inventory(models.Model):
    _name = 'inventory.module'
    _description = 'This is an inventory module, here you can manage your stock and logistics.'

    reference = fields.Char(string='Reference')
    contact = fields.Char(string='Contact')
    schedule_date = fields.Date(string='Scheduled Date')
    source_doc = fields.Char(string='Source Document')
    company = fields.Char(string='Company')
    status = fields.Selection([
        ('draft', 'Draft'),
        ('waiting', 'Waiting'),
        ('ready', 'Ready'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled'),
    ], string='Status')
