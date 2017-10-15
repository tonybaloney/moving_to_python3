class Product:
    label = ''
    price = 0.0
    discount = 10

    def __init__(self, label, price, discount):
        self.label = label
        self.discount = discount
        self.price = price

    @property
    def discounted_price(self):
        return round(self.price * (1.-float(self.discount)/100.), 2)

    def __str__(self):
        # apply discount
        if self.discount > 0:
            return "{0} - {1}% off. Was ${2}, now ${3}!".format(
                self.label,
                self.discount,
                self.price,
                self.discounted_price)
        else:
            return "{0} - ${1}".format(
                self.label,
                self.price)
