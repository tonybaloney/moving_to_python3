from tinydb import TinyDB, Query

from wiredbraincoffee.config import DB_LOCATION
from wiredbraincoffee.models import Product, Store


class ShopController:
    def __init__(self):
        pass

    def view(self, context):
        db = TinyDB(DB_LOCATION)
        Products = db.table('products')
        Stores = db.table('stores')

        products = map(lambda p: Product(p.doc_id, p['label'], p['price'], p['discount']), Products)

        # Convert the stores to store models
        stores = map(lambda store: Store(name=store['name'], 
                                         city=store['city'], 
                                         state=store['state']), 
                     Stores)

        return {
            'products': products,
            'stores': stores}

    def view_item(self, context, id=None):
        db = TinyDB(DB_LOCATION)
        p = db.table('products').get(doc_id=id)
        Stores = db.table('stores')
        product = Product(p.doc_id, p['label'], p['price'], p['discount'])

        # Convert the stores to store models
        stores = map(lambda store: Store(name=store['name'],
                                         city=store['city'],
                                         state=store['state']),
                     Stores)

        return {
            'product': product,
            'stores': stores}
