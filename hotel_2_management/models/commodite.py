from odoo import api, fields, models

class Commodite(models.Model):
    _name = 'hotel.batiment.chambre.commode'
    _description = 'Commode'
    _rec_name = 'name'

    name = fields.Char(string="Id", required=True)
    libelle = fields.Char(string="Nom de la commode")
    description = fields.Text(string="Description")
    type_chambre_ids = fields.Many2many('hotel.batiment.chambre.type', string="Type de Chambre")
    