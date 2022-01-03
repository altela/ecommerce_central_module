# -*- coding: utf-8 -*-
from odoo import api, fields, models

class ProductInherited(models.Model):
    _inherit = "product.template"

    x_show_in_ecommerce = fields.Boolean()
    x_description_sale_ecommerce = fields.Text()
    x_testing = fields.Text()