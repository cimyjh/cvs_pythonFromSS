#snack.py
from product import Product

class Snack(Product):
    _name = '과자'
    _init_file_name = 'snack.json'

    def __init__(self):
       super().__init__(self._name, self._init_file_name)