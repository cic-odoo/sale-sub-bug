# -*- coding: utf-8 -*-
{
    'name': "sale_sub_bug",

    'summary': """
        Calls super on _prepare_invoice_data() to recreate bug""",

    'description': """
        Calls super on _prepare_invoice_data() to recreate bug
    """,

    'author': "Odoo",
    'website': "http://www.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale_subscription'],

    # always loaded
    'data': [
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
