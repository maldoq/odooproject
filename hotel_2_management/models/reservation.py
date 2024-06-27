from odoo import api, fields, models

class Reservation(models.Model):
    _name = 'hotel.reservation'
    _description = 'Reservation'
    _rec_name = 'name'

    name = fields.Char(string="Numero de Réservation", required=True)
    client_id = fields.Many2one('hotel.client', string="Clients")
    bedroom_id = fields.Many2one('hotel.batiment.chambre', string="Chambre")
    space_id = fields.Many2one('hotel.batiment.espace', string="Espace réservé")
    amount = fields.Float(string="Montant de la réservation")
    start_date = fields.Datetime(string="Date de début")
    end_date = fields.Datetime(string="Date de fin")
    state = fields.Selection([
        ('unpaid', 'Non payé'),
        ('partial', 'Partielle'),
        ('paid', 'Payé')
    ], string="État")
    rest_amount = fields.Float(string="Reste à payer")
    payment_ids = fields.One2many('hotel.reservation.paiement', 'reservation_id', string="Paiements")
