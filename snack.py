#snack.py
from product import Product

class Snack(Product):
    _name = '과자'

    def __init__(self, cursor):
       super().__init__(self._name, cursor)