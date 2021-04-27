def apple_deal(num_apples, price):
    return ((num_apples // 3) * 2 + (num_apples % 3)) * price

def banana_deal(num_bananas, price):
    return ((num_bananas // 3) * 100 + (num_bananas%3) * price)

def checkout(items, prices):
    counts = {}
    total = 0
    deals = {'A': apple_deal, 'B': banana_deal}
    for i in items:
        if i in prices:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1
        else:
            raise Exception("Unexpected item in the bagging area! (" + i + " not in pricing list.)")
    
    for c in counts:
        if c in deals:
            total += deals[c](counts[c], prices[c])
        else:
            total += counts[c] * prices[c]

    return total

class Checkout:
    def _deal_n_for_m(self, item, n, m):
        return ((self.counts[item] // n) * m + (self.counts[item] % n)) * self.prices[item]

    def _deal_n_for_price(self, item, n, price):
        return ((self.counts[item] // n) * price) + (self.counts[item] % n) * self.prices[item]

    def _calc_sub_total(self, item):
        if item in self.deals:
            return self.deals[item]()
        else:
            return self.counts[item] * self.prices[item]

    def __init__(self, prices):
        self.prices = prices
        for p in prices:
            if prices[p] < 0:
                print("Warning: Price of " + p + " is negative.")
        self.counts = {}
        self.deals = {'A': lambda: self._deal_n_for_m('A', 3, 2), 'B': lambda: self._deal_n_for_price('B', 3, 100)}
        self.sub_totals = {}

    def scan(self, item):
        if item in self.prices:
            if item in self.counts:
                self.counts[item] += 1
            else:
                self.counts[item] = 1
            self.sub_totals[item] = self._calc_sub_total(item)
        else:
            raise Exception("Unexpected item in bagging area! (" + item + " is not available in the price list.)")

    def total(self):
        return sum(self.sub_totals.values())
        