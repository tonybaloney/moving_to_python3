# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import wiredbraincoffee.controllers.home as home
home.DB_LOCATION = 'test_data.json'

controller = home.HomeController()
model = controller.view(None)


def test_view_data():
    product_names = [p.label for p in model['offers']]

    assert 'Coffee Beans' in product_names


def test_product_offers_unicode():
    product_names = [p.label for p in model['offers']]

    assert 'Coffee Ground ☕️' in product_names

    product_text = [p.text for p in model['offers']]
    assert 'Coffee Ground ☕️ - 10% off. Was $2.99, now $2.69!' in product_text
