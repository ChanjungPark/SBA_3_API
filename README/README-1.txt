OOP에서

class, instance

class on Disk( staic - resource )
instance on Memory( dynamic - resource )
생성자(constructor) 외에는 instance 를 만들 수 없다.

생성자는 (대문자로 시작하는)클래스명에 parameter - zone 이라 불리는 () 구조

instance = Constructor(param)

notation : 표기법 a = '1' (str) a = 1 (int) a = 1.0 (float)
annotation : 주석

JavaScript, C-Java, @static
constant => const, static,
variable => let, int~,

data -> constant + variable => state

variable 은 change 요소를 가지고 있는 정의 -> True
constant 는 change 요소를 가지고 있지 않은 정의 -> False

state 를 종류에 따라 (추상화) : 4가지로 분류, 
CRUD(create data, read data, update data, delete data)

REST(Representational State Transfer)
6가지 조건
1) CS 구조
2) stateless : 
    클라이언트의 context 가 서버에 저장되어서는 안된다
    client context - True
    server context - False
3) 캐시 처리 기능(Cacheable)
4) 중간 서버 (예) WAS(tomcat))
5) URI 를 사용하여 data를 JSON 형식으로 전송


SQL : Language

-----------------------------------------------------------------
app.py

CS구조 -> 서버 : SBA_API, 클라이언트 : SBA_UI  
상태 저장 X -> 쿠키나 세션에 저장 X              
uri 사용 -> URL = URI/search=hyper + JSON      
flask로 중간서버 사용                          

=> REST 입니다
-----------------------------------------------------------------

controller에 REST 설정한 부분까지가 2주차 MVC의 종료입니다.

3주차 Model로 학습전환합니다.
Model 에서 AI 에 대한 알고리즘 학습을 주로 합니다.