# -*- coding: utf-8 -*-
{
    'name': "erpvtech_smart_hotel",

    'description': """
        Hotel Management
    """,

    'author': "Erp VTect",
    # 'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Hotel Management',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'product', 'account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}