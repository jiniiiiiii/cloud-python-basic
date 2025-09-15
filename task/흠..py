# 변수

kor, eng, math = 0, 0, 0

count =0
data_list  = []

# 입력 값에 대한 검증
def check_num(tmp):
    while True:
        try:
            num = int(input(tmp))
            if 0 <= num <= 100: 
                return num
            else:
                print("1~100 사이 정수를 입력하세요. ")
            
        except ValueError:
            print("정수를 입력하세요.")




def __init__main__():
    count = int(input("인원 입력: "))
    for i in range(count):
        name = input("이름 입력 : ")
        kor = check_num("국어 점수 : ")
        eng = check_num("영어 점수 : ")
        math = check_num("수학 점수 : ")
        data_list.append([name, kor, eng, math])

    
print(data_list)

# 출력에 대한 부분 
def print_data():
    # for i in range(len(data_list[i])):    # 호출도 안되었는데 출력함. 
    #     print(data_list[i][0])
    for person in data_list:
        print(person[0])
        
print_data()