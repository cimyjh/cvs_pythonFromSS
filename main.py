#main.py
from coffee import Coffee
from snack import Snack
from printText import PrintText
import sys

if __name__ == '__main__':
    print('1:커피, \t2:과자')
    choice = input('구동할 자판기를 선택 하세요 >> ').strip()

    if choice == '1':
        vm = Coffee()

    elif choice == '2':
        vm = Snack()

    else :
        print(PrintText.select_falut)
        sys.exit(-1)

    try:
        vm.run()
    except KeyboardInterrupt:  #동전을 넣어주세요에서 Enter key를 누르면 프로그램 종료
        print(PrintText.exit_msg)
        sys.exit(0)
