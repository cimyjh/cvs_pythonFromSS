#coffee.py
from product import Product

class Coffee(Product):
    _name = '커피'
    
    def __init__(self, cursor):
        super().__init__(self._name, cursor)