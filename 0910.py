# p38 ~ 57(까지 예정)
##########################################
# 변수
##########################################

#규칙
# 1. 숫자로 시작하면 안됨. 
# 2. 예약어는 변수로 사용 불가능. if, for ..


# 변수 기본 
'''a = 1; b=2;
print(a)    # 출력 1
print("----------------")

print(a,b)  # 출력1 2
print("a=",a,"b=",b)    # 출력 a= 1 b= 2

# 문자열 연결
print("123"+"456")  # 출력 123456
#print("a="+a+"b="+b)    # 오류 발생 why? -> 문자열+숫자(변수)는 불가능. 
print(f"a={a},b={b}")   # f는 포멧지정. {}안에 수식 및 변수 사용 가능. 출력: a=1,b=2
print(f"a={a},b=2")  # 블록 설정해주고 하면 좋다는데? '''


# 변수형 format
'''
%(자릿수)d : 정수형
%(자릿수).(소수점자리수)f : 실수형
%(자릿수)s : 문자열
'''

# 1
'''a = 1; b=200;
print("\t\"a=%3d\"" %a) #         a=  1
print("b=%3d" %b) # b=200

print("\t\"a=%3d\"" %a) # 이건 뭐지? 
'''

#
'''num1 = 35; num2=35.5
print("상수 : %f" %num1) #상수 : 35.000000
print("상수 =:%5.1f" %num2) #상수 : 35.5 -> 전체 5자리, 소수점 1자리
print("상수 =:%5.2f" %num2) #상수 :35.50 -> 전체 5자리, 소수점은 2자리.
'''
#
'''
str = "밥먹고 나니 졸리죠?"
print("%s\n" %str)  # 밥먹고 나니 졸리죠? -> 자릿수가 적으면 영향 x 혹은 글자수가 더 많으면 영향 x
print("%5s\n" %str)  # 밥먹고 나니 졸리죠?
print("%20s\n" %str)  #          밥먹고 나니 졸리죠?
'''

# 형변환 
'''
int() : 정수형 변환
float() : 실수형 변환
str() : 문자열형 변환
'''

'''print(int(35+35.1)) # 70 -> 정수형으로 변환
print(float(35+35.1)) # 70.1 -> 실수형으로

kor = 80
eng = 75
math = 60
print("국어:%3d"%kor, "\t영어:%3d" %eng, "\t수학:%3d" %math)
print("국어:%3d \t영어:%3d \t수학:%3d" %(kor,eng,math)) # 출력 국어: 80        영어: 75        수학: 60
'''
# .format : 이것 안에서 
'''print("국어 : {}점,\t영어:{}점,\t수학:{}점" .format(kor,eng,math))  # 국어 : 80점,    영어:75점,      수학:60점
'''
# 숫자 입력 -> input으로 입력받으면 int로 형변환 
'''
score_kor = int(input("국어 점수 입력(100이하의 수): "))    # or 입력후 다시 int(score_kor)
score_eng = int(input("영어 점수 입력(100이하의 수): "))
score_math = int(input("수학 점수 입력(100이하의 수): "))
sum = score_kor + score_eng + score_math

print("합계는 %3d점" %sum)
'''
# 문자열 배열 
'''str ="안녕하세요."
print(str[0])  # 안
print(str[1])  # 녕
'''

# 56p 이스케이프 코드

################################################33
# 연산자
#############################################
'''
1. 산술연산자 : +, -, *, /, //(몫), %(나머지), **(제곱)
2. 비교연산자 : >, <, >=, <=, ==(같다), !=(같지 않다) -> 출력값을 True or False
3. 논리연산자 : and, or, not
4. 비트연산자 : &(and), |(or), ^(xor), ~(not), <<, >>  -> 출력값을 2진수로. 0 or 1
    4.1. 시프트연산자 : <<, >> -> 2진수로 변환 후 좌측 혹은 우측으로 이동. ex) 0001 << 2 -> 0100 (왼쪽으로 2칸 이동)
5. 대입연산자 : =, +=, -=, *=, /=, //=, %=, **=

'''

# 비트 연산자 예 
'''
a = 10; b= 3
t = True; f = False
print(a and b)  # False -> and 둘다 True여야 True
print(a or b)   # True -> or 둘중 하나만 True여도 True
print(not a)    # False -> 반대
print(a>b and f)    # false
print(not a>b and f) # true
print(a>b or f)  # true
print(not (a>b or f))  # false
'''

# 비트연산자2 -> 각각의 수를 2진수로 변경 후 
'''
a= 5; b =3 # a = 0101, b = 0011 

print(a&b)  # 0001
print(a|b)  # 0111
print(a^b)  # 0110 -> xor 서로 같으면 0, 서로 다르면1 
print(a>>2) # 0101 -> 0001
print(a<<2) # 0101 -> 0100
'''

# 연산자
'''a = 3; b = 2
a += b 
print(a)    # 5
'''

# is , is not 
'''
is : A와 B는 같다 
is not : A와 B는 다르다. 
'''
'''
a = [1,2,3]
b = [1,2,3]
c = a   # 메모리 주소까지 완전히 같아짐. 

print(a ==b)    # 값만 비교하기 때문에 true
print(b==c)     # 값만 비교하기 때문에 true
print(c==a)     # 값만 비교하기 때문에 true

print(a is b)   # 주소 값을 비교해서 false
print(a is c)   # 주소 값을 비교해서 true -> 주소까지 같음. 
print(b is c)   # 주소 값을 비교해서 false 
'''


# 멤버 연산자 in. -> 안에 들어있는가 확인
'''
list = [10,20,30,40,50]
x = 20; y = 24

try:    # 구현하고 싶은 문장
    print(x in y)
    print(x not in y)
except:     # 구현하고 싶은 문장에 Error가 발생한 경우 실행 문장
    print(x in list)    # true -> list 안 있음. 
    print(y in list)    # false 
    print(y not in list)    # true -> list안 없. '''
    
    
# if문 짧게 
'''
# 1기본. 조건이 참이면 왼쪽이 기준. -> if문 왼쪽이 기준
a = 5
res = "Even" if a % 2 == 0 else "Odd"   # 나머지가 0이면 Even, 0이 아니면 Odd
print("res: ", res) # 거짓이므로 Odd 출력

#res2 = "양수" if a>0 else "음수" else if a<0 "음수" #-> 이건 뭔지 잘 모르겠음.

# 리스트 버전 -> 거짓,참
n = 5
res = ["Odd", "Even"][int(n%2==0)]  # n이 짝수면 True(1), 홀수면 False(0)
print(res)  # Even 출력? odd가 출력된다는데 

# 튜플 버전 
n = 5
res=("Odd","Even")[n%2 ==0]  # 거짓, 참  [조건식] --> 조건식의 결과가 거짓인가 참인가
print(res)  # 조건이 거짓 -> 거짓에 해당하는 Odd가 출력

# 딕셔너리 버전 -> 키로 따라 감. 
m=3; n =5 
res = {True:m, False:n}[m>n]    # 거짓이므로 n출력 -> 5
print(res)

res = {False:n, True:m}[m>n]    # 거짓이므로 n출력 -> 5
print(res)'''


##################################
# if조건문
##################################

# 여러 줄 줄바꿈 출력
print("""
if조건: 
    실행식
else 
    실행식
      """)

kor = 80 
if kor > 90:
    print("oh~~~~"); 
else: 
    print("더 분발하세요")
    