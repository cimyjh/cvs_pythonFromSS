#coffee.py
from product import Product
import json

class Coffee(Product):
    _name = '커피'
    _init_file_name = 'coffee.json'
   
    def __init__(self):
        super().__init__(self._name, self._init_file_name)