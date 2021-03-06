# -*- coding: utf-8 -*-
# © 2016 Robin Keunen, Coop IT Easy SCRL fs
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    display_weight = fields.Float(
        'Display Weight',
        related='product_id.display_weight'
    )

    display_unit = fields.Many2one(
        'product.uom',
        'Weight Unit',
        related='product_id.display_unit'
    )
