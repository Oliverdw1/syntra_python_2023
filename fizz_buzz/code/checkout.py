class CannotAddItemWithoutPriceError(Exception):
    def __init__(self, message="You can not add an item without a price"):
        self.message = message
        super().__init__(self.message)

class Checkout():
    def __init__(self):
        self.prices = {}
        self.discounts = {}
        self.items = {}
        self.total = 0


    def add_item_price(self, item, price):
        self.prices[item] = price


    def add_item(self,item):
        if self.prices.get(item, False):
            if item in self.items:
                self.items[item] += 1
            else:
                self.items[item] = 1
        else:
            raise CannotAddItemWithoutPriceError

    def calculate_total(self):
        total = 0
        #for i in self.items:
         #   self.total += self.items[i] * self.prices[i]
        for item, number in self.items.items():
            if item in self.discounts:
                qty = self.discounts[item]["qty"]
                qty_for_price = self.discounts[item]["qty_for_price"]
                times_discounted_price = number // qty
                items_full_price = number % qty
                total += (times_discounted_price * qty_for_price + items_full_price) * self.prices[item]
            else:
                total += number * self.prices[item]
        return total

    def add_discount_rules(self,item, qty, qtyForPrice):
        self.discounts[item] = {"qty": qty,
                                "qty_for_price":qtyForPrice}



checkout = Checkout()
print(checkout.calculate_total())
checkout.add_item_price("a", 10)
checkout.add_item_price("b", 5)
checkout.add_discount_rules('a',4,3)
checkout.add_item("a")
checkout.add_item("a")
checkout.add_item("a")
checkout.add_item("a")
checkout.add_item("b")
checkout.add_item("b")
checkout.add_item("b")
checkout.add_item("b")
print(checkout.calculate_total())