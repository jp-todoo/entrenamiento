# -*- coding: utf-8 -*-
{
    'name': "entrenamiento",

    'summary': """
        Este módulo permite midificar los modelos de entrenamiento de su empresa para un mejor         funcionamiento""",

    'description': """
        Este es el módulo que su empresa debe tener para mejorar la gestión de entrenamiento para empleados, usuarios y contactos
    """,

    'author': "Jonathan",
    'website': "http://www.todoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'web site',
    'version': '1.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    #'demo': [
    #    'demo/demo.xml',
    #],
        "installable": True,
}
