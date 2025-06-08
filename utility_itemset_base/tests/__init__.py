from odoo.tests.common import TransactionCase
from .services.huim import compute_high_utility_itemsets

class TestHUIM(TransactionCase):

    def test_basic_itemset_mining(self):
        transactions = [
            {'items': [{'product_id': 1, 'utility': 100}, {'product_id': 2, 'utility': 200}]},
            {'items': [{'product_id': 1, 'utility': 100}, {'product_id': 3, 'utility': 50}]},
        ]

        min_utility = 150
        results = compute_high_utility_itemsets(transactions, min_utility)

        itemsets = [set(r['items']) for r in results]
        expected = [set([1, 2]), set([2]), set([1, 3]), set([1])]

        for expected_itemset in expected:
            self.assertIn(expected_itemset, itemsets)
