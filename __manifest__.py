# -*- coding: utf-8 -*-
{
    'name': "Odoo RESTAPI",

    'summary': """
        Odoo RESTAPI""",

    'description': """
        Odoo REST API
    """,

    'author': "Tho Dinh",
    'website': "https://github.com/thodinh/odoo-rest-api",
    'category': 'developers',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],

    "application": True,
    "installable": True,
    "auto_install": False
}