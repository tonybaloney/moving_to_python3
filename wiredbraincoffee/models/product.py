PRODUCT_IMAGES = {
    'Beans': '/static/img/beans.jpg',
    'Ground': '/static/img/grounds.jpg'
}


class Product:
    '''
    A simple model for holding a product in the store
    '''
    id = None
    label = ''
    price = 0.0
    discount = 10

    def __init__(self, id, label, price, discount):
        self.id = id
        self.label = label
        self.discount = discount
        self.price = price

    @property
    def discounted_price(self):
        '''
        Get the discounted price, rounded to 2dp
        '''
        return round(self.price * (1.-float(self.discount)/100.), 2)

    @property
    def image(self):
        '''
        Get an image for the product, we mostly sell beans and ground coffee,
        so just use generic images for those
        '''
        for category, image in PRODUCT_IMAGES.iteritems():
            if category in self.label:
                return image
        return '/static/img/product.jpg'

    def __str__(self):
        # If the product has a discount, show original price
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
