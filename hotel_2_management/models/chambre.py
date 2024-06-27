from odoo import api, fields, models, _
from odoo.exceptions import UserError

class Room(models.Model):
    _name = 'hotel.batiment.chambre'
    _description = 'Chambre'
    _rec_name = 'name'

    image = fields.Image(string="Aperçu")
    name = fields.Char(string="Id", required=True, readonly=True, default='New')
    nom = fields.Char(string="Identification de la chambre")
    description = fields.Text(string="Description")
    place_number = fields.Integer(string="Nombre de place")
    base_price = fields.Float(string="Prix par jour")
    building_id = fields.Many2one('hotel.batiment', string="Batiment", ondelete='cascade')
    type_id = fields.Many2one('hotel.batiment.chambre.type', string="Type de chambre")

    @api.model
    def create(self, vals):
        building = self.env['hotel.batiment'].browse(vals['building_id'])
        if building and len(building.chambre_ids) >= building.max_bedrooms:
            raise UserError(_('Le nombre maximum de chambres pour ce bâtiment est atteint.'))
        
        # Génération de l'ID de la chambre
        if vals.get('name', 'New') == 'New':
            building_prefix = str(building.name).zfill(2)
            existing_rooms = self.search_count([('building_id', '=', vals['building_id'])])
            room_number = existing_rooms + 1
            vals['name'] = f"{building_prefix}-{room_number}"
        return super(Room, self).create(vals)
