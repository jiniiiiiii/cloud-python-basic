# 일요일(09.14)까지 제출하세요

'''
[조건]
1. 이름, 국어, 영아, 수학, 총점, 평균, 결과 중 필요한 데이터만 입력받는다. 
2. 입력 받을 인원은 최소 3명 ~ 무한대
3. 함수, 모듈 사용

출력은 다음과 같다. 
##########################################
이름    국어    영어    수학    총점    평균    결과
-------------------------------------------------   
홍길동  90      80      70     250     40.5     F
.
.
.
-------------------------------------------------
0명     국어합  영어합  수학합      .     평균
'''



'''
# 변수
kor, eng, math = 0, 0, 0
avg, sum = 0.0, 0.0
name = ""
grade = ''
'''


# 빈 딕셔너리 생성
data_list = {}

try:
    # 입력받을 인원 수를 정수형으로 변환
    human_count = int(input("입력받을 인원 수를 입력하세요. (숫자만) : "))

except ValueError:
    # 숫자가 아닌 경우 ValueError 발생, 사용자에게 다시 입력 요청
    print("숫자만 입력해 주세요.")
else:
    # 입력받은 인원 수만큼 반복
    for i in range(human_count):
        print(f"\n--- {i+1}번째 학생 정보 입력 ---")
        
        # 이름 입력
        name = input("이름: ")
        
        # 과목별 점수 입력 및 정수형 변환
        try:
            #print("점수를 입력해주세요.")
            kor = int(input("국어 점수: "))
            eng = int(input("영어 점수: "))
            math = int(input("수학 점수: "))

        except ValueError:
            print("점수는 숫자로 입력해야 합니다. 다시 시작해 주세요.")
            # 오류 발생 시 현재 학생 정보 입력 중단 및 다음 반복으로 이동
            continue 

        # 총점 및 평균 계산
        total_sum = kor + eng + math
        avg = total_sum / 3

        # 등급 환산 
        if avg >= 90 : 
            grade ='A'

        elif avg >= 80 : 
            grade ='B'

        elif avg >= 70 : 
            grade ='C'

        elif avg >= 60 : 
            grade ='D'

        else :
            grade ='F'

        # 각 학생의 정보를 담을 딕셔너리 생성
        student_data = {
            'kor': kor,
            'eng': eng,
            'math': math,
            'sum': total_sum,
            'avg': avg, 
            'grade': grade
        }
        
        # data_list 딕셔너리에 학생 이름(key)과 정보(value) 저장
        data_list[name] = student_data



# 모든 데이터 입력 후 결과 출력
# 출력 확인
# print(data_list)


# 출력 
print("########################################################")
print("이름\t 국어\t 영어\t 수학\t 총점\t 평균\t 결과\t")
print("--------------------------------------------------------")

# data_list 딕셔너리를 순회하며 각 학생 정보 출력
for name, data in data_list.items():
    # 평균 점수를 소수점 첫째 자리까지 표시
    avg_formatted = f"{data['avg']:.1f}"

    # 각 항목을 탭(\t)으로 구분하여 정렬
    print(f"{name}\t {data['kor']}\t {data['eng']}\t {data['math']}\t {data['sum']}\t {avg_formatted}\t {data['grade']}")

print("--------------------------------------------------------")
#print(0명     국어합  영어합  수학합      .     평균) # 어캐  출력함. 
