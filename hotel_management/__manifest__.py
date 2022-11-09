# -*- coding: utf-8 -*-
{
    'name': 'Hotel Management',
    'version': '15.0.1.0.0',
    'category': '',
    'sequence': -100,
    'author': 'Meenu M',
    'company': 'Socius Innovative Global Brains Pvt.Ltd',
    'summary': 'Record Hotel Details',
    "description": """To manage Hotel""",
    'depends': ['base', 'product', 'account', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'security/security_sale.xml',
        'data/cron.xml',
        'wizard/create_booking_view.xml',
        'wizard/booking_report_view.xml',
        'views/product_views.xml',
        'views/hotel_views.xml',
        'views/booking_views.xml',
        'views/sale_order_views.xml',
        'views/account_move_views.xml',



        'reports/report.xml',
        'reports/booking_details.xml',
        'reports/sale_details.xml',


    ],
    'qweb': [],
    "license": "AGPL-3",
    'application': True,
    'installable': True,
    'auto_install': False,
}
