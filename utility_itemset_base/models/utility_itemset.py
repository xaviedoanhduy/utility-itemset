# Copyright 2025 Do Anh Duy (doanhduyxavie@gmail.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import models, fields


class UtilityItemset(models.Model):
    _name = "utility.itemset"
    _description = "High Utility Itemset"

    item_ids = fields.Many2many("product.product", string="Items")
    utility = fields.Float("Total Utility")
