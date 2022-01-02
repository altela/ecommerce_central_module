# -*- coding: utf-8 -*-
from odoo import api, fields, models


class SempoaEcommmerce(models.Model):
    _name = "sempoa.ecommerce"
    _description = "Sempoa Ecommerce"

    x_show_in_ecommerce = fields.Boolean(default='False')
    x_description_sale_ecommerce = fields.Text()

