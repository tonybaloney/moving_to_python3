from tinydb import TinyDB, Query

from wiredbraincoffee.models import Product, Store


class HomeController:
    def __init__(self):
        pass

    def view(self, context):
        db = TinyDB('db.json')
        Products = db.table('products')
        Stores = db.table('stores')

        products_with_discount = filter(lambda p: p['discount'] > 0., Products)
        offers = []
        # Get the offers as classes
        for offer in products_with_discount:
            # Apply discount to price
            o = Product(offer['label'], offer['price'], offer['discount'])
            offers.append(o)

        # Convert the stores to store models
        stores = map(lambda store: Store(name=store['name'], 
                                         city=store['city'], 
                                         state=store['state']), 
                     Stores)
        number_of_offers = len(products_with_discount)
        if number_of_offers == 1:
            offer_message = "We have only 1 offer this month"
        else:
            offer_message = "We have lots of offers this month"

        return {
            'offers': offers,
            'offermessage': offer_message,
            'stores': stores}
