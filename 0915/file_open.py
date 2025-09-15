'''
[파일 여는 방법]
- 파일 포인터 = open("파일경로 및 파일명", "모드")
- 모드
    - r : 읽기
    - w : 쓰기, 커서 앞
    - a : 쓰기, 커서 뒤
    - x : 쓰기, 파일이 없을 때 생성. 만일 생성하고자하는 파일이 존재시 에러가 발생함. 
    
- 메서드 
    - .read(n) : n번째 문자 읽음
    - .read([n]) : 지정된 갯수만큼 문자를 읽어옴. 생략할 경우 모두
    - readlines() : line list 로 읽어옴
    - readline() : 한 줄씩 텍스트로 읽어옴 
  
 - 커서 이동
    - seek(p) : p로 지정된 위치에 커서 이동
    
- 파일 닫기
    - 파일 포인터.close()

- 파일 쓰기
    - write("파일에 쓸 텍스트") --> 줄이 바뀌지는 않음 
    - writelines(list) -> 리스트 형식의 데이터
- 
'''

### 파일 열기
'''try: 
    fp=open("D:\\workspace\\vProject-1\\cloud-python-basic-1\\0915\\sample.txt")    # 절대 경로를 적어주니 됨. 상대는 안됨. 왜?
    #print(fp.read())   # fp.read(3) 파일의 3번째 문자 출력 // fp.read() 모든 문자 출력
    print(fp.readline(3))   # 0번째부터 2번째까지 출력함. 
    print(fp.readlines(3))      # 리스트 형식으로 읽음 -> ['ant go home\n']
    
    #i = fp.readlines()
    for i in fp:        # readlines를 readline처럼 출력
        print(i)
    
except :
    print("없어 없다고")
    
finally:
    fp.close()
'''    

### 파일 쓰기
'''
fp = open("D:\workspace\vProject-1\cloud-python-basic-1\0915\sample.txt", "rt", encoding='uft-8')
print(fp.read(1))
fp.seek(3)
print(fp.read(1))
print(fp.tell)

fp.close()
'''

# rw 옵션이면 에러가 남. 
'''
fp = open("D:/workspace/vProject-1/cloud-python-basic-1/0915/sample2.txt", "wt", encoding='UTF=8') # 만일 없는 파일로 경로를 잡으면 파일이 알아서 생김. wt 옵션일 때
fp = open("D:/workspace/vProject-1/cloud-python-basic-1/0915/sample4.txt", "x", encoding='UTF=8') # 없는 파일을 생성하기 때문에 존재하면 에러남. 

fp.write("[\n")
fp.write("\t[홍길동, 2, 3, 4],\n")
fp.write("\t[진짜길동, 2, 3, 4]\n")
fp.write("\n]")
fp.close()'''



### 리스트를 이용한 쓰기 
#content = ["홍길동", "김김김", "박박"]      # 홍길동김김김박박   이렇게 입력되네 
content = [
    ["홍길동", "김김김", "박박"],
    ["1", "2", "3"]
]
fp = open("D:/workspace/vProject-1/cloud-python-basic-1/0915/sample2.txt", "wt", encoding='UTF-8')
fp.writelines(str(content))     # 문자열 변환이 필요함 -> [['홍길동', '김김김', '박박'], ['1', '2', '3']]
fp.close()


# 파일 오픈 
# 파일 읽기 : read(), readline(), readlines()
# 파일 쓰기 : write("문자열"), writelines(list)
# 커서 위치 : seek(), tell()    --> 실사용 예제로 재 수업 ? 






# 아무튼 함수는 추후 테라폼과도 연결 될 거 같다. ? 