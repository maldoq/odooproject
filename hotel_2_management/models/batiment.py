from odoo import models, fields, api, _
from odoo.exceptions import UserError

class Batiment(models.Model):
    _name = 'hotel.batiment'
    _description = 'Batiments de l\'hotel'
    _rec_name = 'name'

    image = fields.Image(String="Aperçu")
    id = fields.Integer(string='ID', readonly=True)
    name = fields.Char(string="Nom du batiment", required=True)
    description = fields.Text(string="Description")
    free_bedrooms = fields.Integer(string="Chambre libre")
    max_bedrooms = fields.Integer(string="Nombre de chambre maximum")
    number_stage = fields.Integer(string="Nombre d'étage")
    chambre_ids = fields.One2many('hotel.batiment.chambre', 'building_id', string="Chambres")

    def action_generate_rooms(self):
        for building in self:
            if len(building.chambre_ids) >= building.max_bedrooms:
                raise UserError(_('Le nombre maximum de chambres pour ce bâtiment est atteint.'))

            room_obj = self.env['hotel.batiment.chambre']
            while len(building.chambre_ids) < building.max_bedrooms:
                room_number = len(building.chambre_ids) + 1
                room_vals = {
                    'name': f"{str(building.name)[:2].upper()}-{room_number}",
                    'building_id': building.id,
                }
                room_obj.create(room_vals)
