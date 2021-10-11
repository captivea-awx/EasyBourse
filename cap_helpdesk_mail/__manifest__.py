# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Captivea Helpdesk Mail',
    'version': '1.0.1',
    'author': "Captivea France",
    'category': 'Services/CapHelpdeskMail',
    'summary': 'Remove Helpdesk\'s weird looking mail and his button',
    'depends': [
        'helpdesk',
    ],
    'description': """
Captivea Helpdesk Mail Override
=================
Remove Helpdesk's weird looking mail and his button.

    """,
    'data': [
        'data/cap_mail_data.xml',
    ],
    'auto_install': True,
    'license': '',
}
