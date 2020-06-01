#main.py
from coffee import Coffee
from snack import Snack
from cupnoodle import CupNoodle
from printText import PrintText
import sys, os.path, sqlite3
import dbinit

if __name__ == '__main__':

    try:
        conn = None
        if not os.path.exists('test.db'):  #프로그램을 처음 실행할 때
            conn = sqlite3.connect('test.db')
            dbinit.init(conn)
        else :       #한번 이상 프로그램을 실행했을 때
            conn = sqlite3.connect('test.db')
            cursor = conn.cursor()

            print('1:커피, \t2:과자')
            choice = input('구동할 자판기를 선택 하세요 >> ').strip()

            if choice == '1':
                vm = Coffee(cursor)

            elif choice == '2':
                vm = Snack(cursor)

            else :
                print(PrintText.select_falut)
                sys.exit(-1)

            try:
                vm.run()
            except KeyboardInterrupt:  #동전을 넣어주세요에서 Enter key를 누르면 프로그램 종료
                print(PrintText.exit_msg)
                sys.exit(0)

    except Exception as ex:
        print('Exception = ', ex.args[0])
    finally : 
        conn.close()