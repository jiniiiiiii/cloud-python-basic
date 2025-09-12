
# 사칙연산 프로그램 만들기 + 예외처리
'''
[조건]
1. 변수명은 num1, num2, op(연산자)
2. 예외처리 
'''

#import mod  # import 파일명 -> 코드 내부에서 함수 선언시 mod.함수명 같은 식으로 선언해야 함. 
from mod import *   # *은 mod에서 모든 함수를 가져오겠다는 뜻. 혹은 필요한 것만 가져올 수도 있음. 

#mod. 으로 변수명 접근 간으


# 전역변수
num1=(input("num1-->"))
num2=(input("num2-->"))
op = input("연산자(+, -, /, *)-->")

# checkNum(num1)   를 먼저 선언하면 안됨. -> 위에서 부터 실행하기 때문

first=checkNum(num1)
sec=checkNum(num2)
print(first,sec)    # 만일 숫자, 문자 입력시 -> 숫자 Fasle 

result = 10
result(first, sec, op) # 현재 op에 대한 검증은 안함. 
print(result)   # 어디선가 값이 꼬였는지 [0, 3, '덧셈의 결과'] 정상적인 입ㄹ력인데 이렇게 나오네


# class 호출시에는 자동 실행해야 함.