from odoo import api, fields, models

class Service(models.Model):
    _name = 'hotel.service'
    _description = 'Service'
    _rec_name = 'name'

    id = fields.Integer(string="ID", readonly=True)
    name = fields.Char(string="Libelle du service", required=True)
    description = fields.Text(string="Description")
    base_price = fields.Float(string="Prix par jour")