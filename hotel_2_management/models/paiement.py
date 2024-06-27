from odoo import api, fields, models

class Payment(models.Model):
    _name = 'hotel.reservation.paiement'
    _description = 'Paiement'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'name'

    id = fields.Integer(string="ID",readonly=True)
    name = fields.Char(string="Numero du paiement", required=True)
    reservation_id = fields.Many2one('hotel.reservation', string="Réservation")
    pay_amount = fields.Float(string="Montant")
    journal_id = fields.Many2one('account.journal', string='Journal')
    
    
    