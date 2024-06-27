# -*- coding: utf-8 -*-
{
    'name': "Gestion Hotelière",

    'summary': """
        Module de gestion d'hotel""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Maldoqaums",
    'website': "http://www.yourcompany.com",

    
    'category': 'Uncategorized',
    'version': '1.3',

    'depends': ['base','account','account_accountant'],

    'data': [
        'views/hotel_batiment_chambre_commode_views.xml',
        'views/hotel_batiment_chambre_type_views.xml',
        'views/hotel_batiment_chambre_views.xml',
        'views/hotel_batiment_espace_views.xml',
        'views/hotel_reservation_views.xml',
        'views/hotel_batiment_views.xml',
        'views/hotel_employe_views.xml',
        'views/hotel_reservation_paiement_views.xml',
        'security/ir.model.access.csv'
    ],
    'installable': True,
    'application': True,
}
