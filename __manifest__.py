# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Central Ecommerce Integration',
    'author': 'Altela Eleviansyah Pramardhika',
    'version': '12.0',
    'summary': 'Integrate Odoo ERP to Central E-Commerce',
    'sequence': 1,
    'description': """Integrate Odoo ERP to Central E-Commerce""",
    'category': 'Website',
    'website': 'https://altela.my.id',
    'depends': [
        'stock',
        'sale_management'],
    'data': [
        'views/product_template_inherited.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
