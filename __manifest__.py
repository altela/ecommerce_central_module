# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Ecommerce Sempoa Integration',
    'version' : '12.0',
    'summary': 'Adding several properties that pulled and integrated to Ecommerce created by Sempoa',
    'sequence': 1,
    'description': """Adding several properties that pulled and integrated to Ecommerce created by Sempoa""",
    'category': 'Website',
    'website': 'https://altela.my.id',
    'depends' : [
        'stock'],
    'data': [
        'views/productInherited.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
