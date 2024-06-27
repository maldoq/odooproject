from odoo import api, fields, models, _

class Employe(models.Model):
    _name = 'hotel.employe'
    _description = 'Employé'
    _rec_name = 'name'

    id = fields.Integer(string="ID",readonly=True)
    name = fields.Char(string="Nom de famille")
    firstname = fields.Char(string="Prénoms")
    birthday = fields.Date(string="Date de naissance")
    contact = fields.Char(string="Numero de téléphone")
    email = fields.Char(string="Email")
    building_id = fields.Many2one('hotel.batiment',string="Batiment")