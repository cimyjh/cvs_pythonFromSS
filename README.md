# cvs_pythonFromSS
쌍용학원에서 진행


- main: 
  - 프로그램 실행을 하며 세부 메소드는 클래스 단위로 내려보낸다.
  - vm.run을 통해 하위클래스(커피, 스낵) -> 상위클래스의 run() 메소드 실행
  - 예외처리를 사용해서 프로그램 종료를 정의 했다.

                 
- printText:  
  - enum과 같은 효과를 냈다.
  - UI에 대한 인터페이스를 구현했다.
  - 이것을 product에서 불러오도록 했다.
  - product의 코드가 간결해지고 일정한 규칙을 갖게 된다.


- product:  
  - 상위 클래스이다.
  - run(): main에서 호출, coin의 값을 입력받는다. 예외처리. selectProduct()로 값을 넘긴다.
  - selectProduct(): 제품의 리스트를 for문으로 보여준다. selectNumber를 입력받는다. selectNumber파라미터를 selectName(), selectValue, payment()로 보낸다.
  - selectValue(): 계산 후 price반환
  - selectName(): 계산 후 pname반환

  - payment(): 잔고 계산. 돈 부족 했을 때의 예외처리


- json작업
  - product __init__에서 json with open 한다.
  - _productName, _productValue로 json으로 받은 값을 파이썬에서 저장한다.