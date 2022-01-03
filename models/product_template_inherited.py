# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ProductTemplateInherited(models.Model):
    _inherit = "product.template"

    x_show_in_ecommerce = fields.Boolean(store=True)
    x_description_sale_ecommerce = fields.Text(store=True)
