#snack.py
from product import Product

class Snack(Product):
    _name = '과자'

    def __init__(self):
        self._productName = {'1' : '오감자', '\t2' : '오징어땅콩', '\t3' : '빼빼로', '\t4' : '칸쵸', '\t5' : '맛동산'}
        self._productValue = {'1': 400, '2': 500, '3' : '600', '4': 500, '5' : 600}
        super().__init__(self._name, self._productName, self._productValue)