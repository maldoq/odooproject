from odoo import api, fields, models

class Type_Room(models.Model):
    _name = 'hotel.batiment.chambre.type'
    _description = 'Type de chambre'
    _rec_name = 'name'

    name = fields.Char(string="Id", required=True)
    libelle = fields.Char(string="Libellé")
    description = fields.Text(string="Description")
    base_price = fields.Float(string="Prix par jour")
    commodite_ids = fields.Many2many('hotel.batiment.chambre.commode', string="Commode")