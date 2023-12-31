# -*- coding: utf-8 -*-
{
    'name': "Sales_Inherit",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Kunal Roy",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale','sale_management','website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/sales_order_views.xml',
        'views/templates.xml',
        'views/website_form.xml',
        'report/report.xml',
        'report/sale_report_inherit.xml',

    ],
    'assets': {
        'web.assets_frontend': [
            'sales_inherit/static/src/js/sales_js/sales_website.js'
        ],
    },
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
