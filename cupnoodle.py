#cupnoodle.py
from product import Product
class CupNoodle(Product):
    _name = '컵라면'
    _init_file_name = 'cupnoodle.json'

    def __init__(self):
        super().__init__(self._name, self._init_file_name)
