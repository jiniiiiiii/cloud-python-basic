'''
[조건]
구구단을 출력하되, 내가 입력한 단만 출력함. 
'''

#print(null)

'''
# 이중 for 문
for i in range(1,10):
    for j in range(2,10):
        if j < 9 :
            print("%3dx%2d=%3d" %(i,j,i*j), end="\t")
        else:   # j가 10인 경우
            print("%3dx%2d=%3d" %(i,j,i*j))'''
            
            
''' 
# 내가 만든거           
for i in range(1,10):
    print(f"==={i}단===")
    for j in range(1,10):
        print("%2d x %2d = %2d" %(i,j, i*j))
        if j==9:
            print("\n")
'''    

global dan

#try:
#    dan=input("출력할 단을 입력해주세요 : ")
    
'''
    print(f"{dan}단을 입력하셨습니다.")
    
except:
    print("다시 입력해주세요")

else:
    print(f"====={dan}단=====")
    for i in range(1,10):
        print("%2d x %2d = %2d" %(dan,i, dan*i))
'''        
# 숫자 입력 검증에 대한 함수
def input_check(input_num):
    while(True):
        if input_num==int():
            dan = input_num
            msg ="숫자가 입력되었습니다. "
            status = 1
            break
        else:
            msg = "숫자외의 값을 입력하였습니다. 다시 입력하세요."
            status =0
            continue
    print(msg)
    return input_num, status


# 모듈화해서 출력 함수
#ef print_gugudan():
 
 
 
 tmp = input("입력")
 tmp = 
 
 
 # 아니 더 어려운데 함수쓸려고 하니까