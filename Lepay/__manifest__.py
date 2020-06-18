# -*- coding: utf-8 -*-
{
    'name': "LePay",

    'summary': """
        Taking inputs from users for validations""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Paidy Kumar",
    'website': "http://......",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Assignment',
    'version': '12.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/templates.xml',
        'views/views.xml',
        'menus/op_menu.xml',
    ],


    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
