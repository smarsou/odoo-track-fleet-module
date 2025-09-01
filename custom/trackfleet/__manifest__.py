# -*- coding: utf-8 -*-
{
    'name': "trackfleet",

    'summary': "Track the fleet and its deliveries.",

    'description': """
This module helps you track your fleet and all deliveries.
    """,

    'author': "JOST",
    'website': "https://smarsou.fr",

    'application': True,

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/trackfleet_truck_views.xml',
        'views/trackfleet_delivery_views.xml',
        'views/trackfleet_menus.xml',
        'demo/trackfleet_truck_demo.xml',
        'demo/trackfleet_delivery_customer_demo.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml'
    ],
}

