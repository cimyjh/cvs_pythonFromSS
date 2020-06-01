#coffee.py
from product import Product

class Coffee(Product):
    _name = '커피'

    def __init__(self):
        self._productName = {'1':'밀크커피', '\t2':'설탕커피', '\t3':'프림커피', '\t4':'블랙커피', '\t5':'원두커피'}
        self._productValue = {'1':300, '2':300, '3' : '400', '4': 200, '5' : 500}
        super().__init__(self._name, self._productName, self._productValue)