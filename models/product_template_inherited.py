# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ProductTemplateInherited(models.Model):
    _inherit = "product.template"

    x_show_in_ecommerce = fields.Boolean(string="Show In Ecommerce", store=True, help="If this checkbox filled, this product will show in Central E-Commerce", ttype="boolean")
    x_description_sale_ecommerce = fields.Text(string="Description Sale Ecommerce", store=True, help="A description of the Product that you want to communicate to your customers. This description will be pulled to E-Commerce", ttype="text")
