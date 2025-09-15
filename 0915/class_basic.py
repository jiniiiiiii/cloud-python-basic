'''
[규칙]
- 클래스명 : 클래스명의 시작은 영문 대문자. 
- 클래스 안 함수 = 메서드 ( or 클래스 함수 )
- 클래스 안 변수 = 클래스 변수, 인스턴스 변수
- ___init___(self, 매개변수 . . ) : 인스턴스의 초기값 지정
'''


### 클래스 기초 ###
# class Class_name:  --> 선언 방법
# clsObj = 클래스명() --> 클래스의 인스턴스화 

## sample
'''class ClsTest: 
    def ___init___(self,a):     # 클래스를 호출하는 순간 자동으로 사용될 거. -> 전역변수의 초기값 지정시 사용
        self.str = a    # self.str은 인스턴스 변수
        
    def prt(self):
        print(self.str)     
        
# 인스턴스 선언 
prtTest = ClsTest("홍길동")     # dclass의 인스턴스로 선언하겠다. 메개변수로 "홍길동" -> 클래스의 a로 홍길동 전달 
# prtTest 는 복사해서 새로 만들었다 생각

prtTest.prt()   # prtTest중에서 prt를 사용해라. -> clsTest의 메서드인 prt를 사용하겠다는 의미. 

# 클래스명 != 인스턴스 명
        '''

## sample2 -> 클래스 변수 vs 인스턴스 변수
'''
class ClsTest: 
    num1 = 10   # 클래스 변수
    def __init__(self,a, b):     
        #self.a = a    # 인스턴스 변수 -> 클래스 변수를 인스턴스 변수안에 사용x ==> 클래스명.클래스변수명 -> ClsTest.num1
        #self.a = ClsTest.num1   # 이렇게 되면 출력 값 12
        ClsTest.num1 = a    # 클래스 변수를 수정함. 
        self.b = b
        #ClsTest.변수명 = a    #혹은 클래스 내에서 변경되지 않을 상수값을 지정할 수도 있음. 
        
    def prt(self):
        # print(f"a+b={self.a+self.b}")
        #return self.a + self.b     # --> 결과 12
        return self.num1 + self.b   # 결과 3
        
# 인스턴스 선언 
# print(ClsTest.num1)     # 클래스 변수를 수정하기 전이므로 10이 나옴. 
# prtTest = ClsTest(1,2)
# #prtTest.prt()      # 이거가 메소드 변수를 바뀌게 함. 
# print(prtTest.prt())    # return self.a + self.b 시 12 반환
# print(ClsTest.num1) # 1 .. 왜 1 ? 10이 나와야하는거 아닌가. --> ClsTest.num1 = a으로 클래스 변수를 수정함. 

# 선언에 대한 비교
print(ClsTest.num)  # 10
prtTest = ClsTest(1,2)  # 10
print(ClsTest.num)  #10
print(prtTest.prt())    # 3
print(ClsTest.num)  # 왜 3 ? 아.. 위에 코드도 바뀌었네...... 
prtTest1 = ClsTest(3,4)
print(ClsTest.num)

'''


### 클래스의 상속 ###
# OverWrite : 부모가 만들어 놓은 것을 고쳐 쓰겠다. 
# class 클래스명(부모_클래스명):
#   -> 부모 클래스의 인스턴스 변수 사용 : self.변수명 
#   -> 부모 클래스의 메서드 사용 : self.메서드명()
class Parent:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def prt(self):
        return self.a + self.b
    
class Child(Parent):      # 클래스명(부모클래스명) --> 부모 클래스명 기재를 통해 상속 가능 
    def add(self, c):
        self.c = c      # 사용하고자 하는 매개변수가 선언되지 않으면 에러남. 
        # 인스턴스를 선언하지 않고 사용해서 
        print(self.a + self.b + self.c) 
        print(self.prt())     # 클래스 안쪽에 사용시에는 self로 부모 메서드 사용

childTest = Child(1,2)      # 인스턴스를 생성할 때는 자식 클래스명에 부모 클래스에 전달할 값을 작성
print(childTest.a)  # 1
print(childTest.b)  # 2
print(childTest.prt())      # 3      --> Child에는 prt 메서드를 만들지 않았지만, 사용가능해짐. 
childTest.add(2)    # 5 -> 1 + 2 + 2  ==> 부모의 인스턴스 변수를 받아옴. 
# 그리고 3 출력. prt에 대한 값. 부모 메서드의 반환값 -> 1+2





## 클래스 오버라이딩 -> 부모 클래스의 내용을 수정해서 사용
print("============구분============")
class Child2(Parent):
    def add (self, a):
        self.c =a
    
    def prt(self, c):
        self.c = c
        print(self.a + self.b + self.c )
        
childTest2 = Child2(1,2)
childTest2.add(10)
childTest2.prt(10)  # 10    --> child2(1,2)로 전달한 1 + 2 + 10 이 됨. 
print(childTest.prt())  # 3 -> 부모 prt 그대로


# 단순한 상속값만 만들 때?  
class ClassT():
    def prt(self):
        self.a = 10
        self.b = 20
        print(self.a, self.b)   # 값 확인용. 
        
print("============구분============")
te = ClassT()   # 클래스 사용하겠다. 
te.prt()    # 10 20 출력

