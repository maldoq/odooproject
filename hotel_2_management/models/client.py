from odoo import api, fields, models

class Customer(models.Model):
    _name = 'hotel.client'
    _description = 'Client'
    _rec_name = 'name'

    name = fields.Char(string="Nom")
    firstname = fields.Char(string="Prenoms")
    email = fields.Char(string="Email")
    contact = fields.Char(string="Contact")
