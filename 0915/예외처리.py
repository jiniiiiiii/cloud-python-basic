'''
[기본 형식 ]
trt: 
    예외가 발생할 수도 있는 실행문 
except 예외 이름 [as value]:
    실행 문
    
except 예외 이름 [as value]:
    실행 문

else: 
    예외가 발생하지 않아씅ㄹ 경우 처리할 문장
    
finally: 
    예외의 발생 여부와 관계없이 처리할 문장

===========주요 예외 이름============
- ValueError : 부적절한 값을 사용했을 경우 or 참조값이 없을 경우 
- TypeError : 다른 형의 연산
- ZeroDivisionError : 나눗셈에서 분모가 0일 경우 
- IndexError : 딕셔너리에서 키가 존재하지 않았을 때 
- FileObjectFormat : 형식 에러? 
'''


### 에러 예제
'''
# ValueError
try:
    num1 = int("a")
    num2 = ["a", "b", "c"]
    print(num2.index("d"))
except ValueError as e:
    print(e)
    
# typeError
try: 
    result =+ 10 + "a"
except TypeError as e:
    print(e)
    
# IndexError
try:
    num3 = ["a","b","c"]
    print(num3[4])
except IndexError as e:
    print(e)

# keyError
try: 
    dict={"name":"Hong", "kor":90}
    print(dict["eng"])
except KeyError as e:
    print(e)
    
    
# nameError
try: 
    num=10
    print(num)
except NameError as e:
    print(e)
    
# ZeroDivisionError
try: 
    result2 = 10/0
    print(result2)
    
except ZeroDivisionError as e:
    print(e)
    
# OverFlowError
try: 
    result3 = 10** 10000
    print(result3/5)
except OverflowError as e: 
    print(e)
    
# FileNotFoundError
try:
    f = open("sssss.txt", "r")
except FileNotFoundError as e:
    print(e)
    
'''


'''
[조건]
- 숫자를 입력받아 정수로 변환
- 변환이 되면 덧셈
- 예외가 발생할 경우 예외 메시지를 출력
- 연산이 종료되었습니다. 
'''

# 아니 종료가 안됨.

'''import keyboard

while (1):
    intData1 = input("정수 입력해라 : ")
    intData2 = input("정수 입력해라 : ")

    try: 
        intData1 = int(intData1) 
        intData2 = int(intData2)
        if (intData1==keyboard.is_pressed('e')) or (intData2==keyboard.is_pressed('e')):  # e 키가 눌리면
            break
    except ValueError:
        print("정수를 입력하세요!!!!!!!!")
        
    else:
        result = intData1 + intData2
        print(f"덧셈결과 : {result}")
    
    finally: 
        print("끝 ~~~~~")'''