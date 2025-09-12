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
            

