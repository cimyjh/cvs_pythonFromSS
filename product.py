#product.py
from printText import PrintText

#자식 제품의 원형 클래스
class Product:
    #자판기 프로그램 가격 상수값
    PRICE_UNIT = 100
    
    _name = ''

    def __init__(self, name, productName, productValue):
        self._name = name
        self._productName = productName
        self._productValue = productValue
        print(PrintText.title % self._name)

    def run(self):
        while True:
            try:
                coin = input(PrintText.input_coin)
                if not coin:   #만일 그냥 Enter key를 눌렀다면
                    raise KeyboardInterrupt
            except ValueError:   #잘못된 값을 넣었다면
                print(PrintText.select_falut)     
            else : 
                self.selectProduct(int(coin))

    def selectProduct(self, coin) :
        #제품의 종류를 리스트로 만들어서 유저에게 보여주자.
        description = ''
        for num, pname in self._productName.items():
            price = self.selectValue(num.strip())
            description += PrintText.product % (str(num), pname, str(price))

        print(description)
        selectedNumber = input(PrintText.select_product)
        price = self.selectValue(selectedNumber)  #번호에 대한 해당 상품의 가격 알아오기

        if price :
            pname = self.selectName(selectedNumber)
            self.payment(coin, int(price), pname)
        else :  #즉 잘못된 번호를 선택했다면
            print(PrintText.select_falut)


    def selectValue(self, inputNum):
        price = 0
        for num, pprice in self._productValue.items():
            if num == inputNum : price = pprice
        
        return price

    def selectName(self, inputNum):
        pname = None
        for num, name in self._productName.items():
            if str(num).strip() == str(inputNum):
                pname = name

        return pname


    def payment(self, coin, price, pname):
        if self.PRICE_UNIT * coin >= price :
            balance = self.PRICE_UNIT * coin - price
            print(PrintText.product_out % (pname, balance))
        else : 
            print(PrintText.not_enough_coin % price)