from odoo import models, fields
from odoo.addons.utility_itemset_base.services.huim import compute_high_utility_itemsets

class HUIMWizard(models.TransientModel):
    _name = 'huim.sale.wizard'
    _description = 'HUIM Wizard for Sale Orders'

    min_utility = fields.Float("Minimum Utility", default=100.0)

    def action_mine(self):
        SaleOrder = self.env['sale.order']
        transactions = []

        for order in SaleOrder.search([]):
            items = []
            for line in order.order_line:
                utility = line.product_uom_qty * line.price_unit
                items.append({
                    'product_id': line.product_id.id,
                    'utility': utility
                })
            transactions.append({'items': items})

        results = compute_high_utility_itemsets(transactions, self.min_utility)

        self.env['utility.itemset'].search([]).unlink()

        for r in results:
            self.env['utility.itemset'].create({
                'item_ids': [(6, 0, r['items'])],
                'utility': r['utility'],
            })

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'utility.itemset',
            'view_mode': 'list',
            'name': 'High Utility Itemsets (from Sales)',
        }
