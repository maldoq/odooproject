from odoo import api, fields, models

class Space(models.Model):
    _name = 'hotel.batiment.espace'
    _description = 'Espace de loisir ou detente'
    _rec_name = 'name'

    id = fields.Integer(string="ID",readonly=True)
    name = fields.Char(string="Nom de l'espace", required=True)
    description = fields.Text(string="Description")