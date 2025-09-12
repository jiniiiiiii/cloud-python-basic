# 리스트에 대해
'''
titList = ["name", "kor", "emg", 'math']
msgList = ["이름", "국어점수", "영어점수", "수학점수"]
cnt = len(titList)
while True:
    dicObj = {}'''


#주소 값에 의한 문제 
'''
resLsit=list()
dict1={}

a=0; b=10;
for j in range(3) :
    for i in range(3):
        # dict1 = {"a":a, "b":b}'''
        
        
###################
# 함수
###################
#def 함수명(): 
#def 함수명(var1, var2...) -> 매개변수 기입

# 기본 예 
'''
def func1(a,b,c):
    
    print(a+1, b+2, c+3)

func1(1,2,3)
'''

# 함수의 return
'''
def func2(a,b):
    return a+b  # 반환값을 지정하겠다. 

result = func2(3,5)
print(f"{result}")   # 출력 8 tip. 여러개의 데이터를 넘겨줄 떄 리스트로 넘겨주는게 좋음

# tip. 전역변수는 가급적이면 지향해라. 앱의 퍼포먼스에 영향을 줌 .
'''

# 전역 변수와 지역 변수
'''
a= 10 
def func():
    global a    #전역변수 -> 값이 처음 호출했을 때만 초기화 됨. 함수 안에서 지역변수를 사용하기 위해서는 global로 선언
    a = a+10    # a = 20
    return a    # 20 반환

res = func()    # res = 20
print(a)    # 20
res = func()    '''


'''
a= 10 
def func():
    a = a+10    # a = 20
    return a    # 20 반환

res = func(10)    # res = 20
print(res)    # 20
print = func(20)    # 30
print(res)  # 30'''


'''a= 10 
def func():
    b =20
    a = a+b 
    return a

res = func(10)    # res 30
print(res)    # 30

res = func(10)   
print(res, b)   # b는 함수 안에서만 사용가능한 지역변수이므로 호출시 오류 남. '''


# 사칙연산 프로그램 만들기 + 예외처리
'''
[조건]
1. 변수명은 num1, num2, op(연산자)
2. 예외처리 
'''

# 전역변수
num1=(input("num1-->"))
num2=(input("num2-->"))
op = input("연산자(+, -, /, *)-->")

# checkNum(num1)   를 먼저 선언하면 안됨. -> 위에서 부터 실행하기 때문

# 반복 작업을 줄여줄 함수 사영 --> 파일로 따로 작성해놓고 main에는 import로 사용
def checkNum(a): 
    try:    # 실행하고자 하는 문장
        num=int(a)
        return num
    except: # try 블럭문에 에러가 있을 경우    
       # print("숫자가 아닙니다.")
       return False     # 예외 처리를 통해 반환 값을 다르게 할 수도 있음. 
        # 0 != False

    # else:   # 에러가 없을 경우. 즉 정상 실행?  
    #     #return 0    # return을 해준다는 얘기는 정상적으로 구동이 되었다는 뜻
    #     print("숫자 변환이 됩니다. ")

    # finally:     # 항상 실행시킬 것
    #     print("항상 감사합니다. ")
                
    # # 이런 try, except. else, finally 가 사용될 때: 데이터베이스 사용시. 
    
#checkNum(num1)  # return 값은 언제가 좋을까? 


def result(a,b,c):
    result_list = []
    msg=""
    res = 0; 
    chk=0   # 오류가 나는 곳에 둘 변수
    if(a==False or b==False):
        "0"     # 숫자를 입력하지 않았을 때
        msg="숫자 입력 오류"
        chk=0       
    else: 
        if c=="+":
            res=a+b
            msg="덧셈의 결과"
        
        elif c =="-":
            res=a-b
            msg="뺼셈의 결과"
        
        elif c =="*":
            res=a*b
            msg="곱셈의 결과"
            
        elif c =="/":
            res=a/b
            msg="나눗셈의 결과"
        
        else: 
            "연산자 오류"
            chk=0
            
    result_list = [chk, res, msg]   # 오류 체크값, 정상적 결과값,정상이나 오류에 대한 메시지 값
    #[0,7,"숫자 입력 오류"]   # 인덱스를 이용해서 정상, 오류에 대한 처리를 함. 
    return result_list  # 만일 글로벌로 선언했으면 return 불필요
            

first=checkNum(num1)
sec=checkNum(num2)
print(first,sec)    # 만일 숫자, 문자 입력시 -> 숫자 Fasle 

result = result(first, sec, op)
print(result)   # 어디선가 값이 꼬였는지 [0, 3, '덧셈의 결과'] 정상적인 입ㄹ력인데 이렇게 나오네