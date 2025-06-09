from odoo import models, fields


class Inventory(models.Model):
    _name = 'inventory.module'
    _description = 'This is an inventory module, here you can manage your stock and logistics.'

    reference = fields.Char(string='Reference')
    contact = fields.Char(string='Contact')
    schedule_date = fields.Date(string='Scheduled Date')
    source_doc = fields.Char(string='Source Document')
    company = fields.Char(string='Company')
    status = fields.Selection(
        selection=[
            ('draft', 'Draft'),
            ('waiting', 'Waiting'),
            ('ready', 'Ready'),
            ('done', 'Done'),
            ('cancelled', 'Cancelled'),
        ],
        string='Status',
    )
    sender = fields.Many2one(
        'res.partner',
        string='Receive From',
        domain="[('is_company', '=', False)]",
    )
    deadline = fields.Date(string='Deadline')
    source_document = fields.Char(string='Source Document')
    operation_type = fields.Many2one(
        'stock.picking.type',
        string='Operation Type',
    )
