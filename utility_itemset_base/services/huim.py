from itertools import combinations
from collections import defaultdict


def compute_high_utility_itemsets(transactions, min_utility):
    utility_itemsets = defaultdict(float)

    for trx in transactions:
        items = trx["items"]
        for r in range(1, len(items) + 1):
            for itemset in combinations(items, r):
                itemset_ids = tuple(sorted(i["product_id"] for i in itemset))
                utility = sum(i["utility"] for i in itemset)
                utility_itemsets[itemset_ids] += utility

    return [
        {"items": list(k), "utility": v}
        for k, v in utility_itemsets.items()
        if v >= min_utility
    ]
