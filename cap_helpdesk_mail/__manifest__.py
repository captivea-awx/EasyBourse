# -*- coding: utf-8 -*-
-{
    'name': "Captivea Helpdesk Mail",

    'summary': """
        Remove Helpdesk\'s weird looking mail and his button""",

    'description': """
Captivea Helpdesk Mail Override
=================
Remove Helpdesk's weird looking mail and his button.

    """,

    'author': "Captivea France",
    'website': "https://www.captivea.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services/CapHelpdeskMail',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'helpdesk'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/cap_mail_data.xml',
    ],

    'installable': True,
    'application': False,
    'auto_install': True,
}
