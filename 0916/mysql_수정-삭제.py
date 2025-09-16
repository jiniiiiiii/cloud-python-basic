import pymysql
import my_db_module


dtList=[]
for i in range(4):
    dtList.append(input())

sql=f"insert into test (name, kor, eng, math) value ('{dtList[0]}', '{dtList[1]}', '{dtList[2]}', '{dtList[3]}')"
print(sql) 


dbObject = dbconn.DBConn("localhost", "root", "1234", "Python")    #1. 연결
conn = dbObj.DBConnect()

if dbObject.execQury(sql):
    print("정상적으로 데이터를 입력하셨습니다. ")
else: 
    print("잠시 서버에 장애가 발생했습니다.")

cursor = conn.cursor()      # 2.데이터베이스에 커서 위치 USE Database
result = cursor.execute(sql)    #3. 데이터베이스에서 쿼리문 실행
conn.commit()       # 4. 설정 적용

cursor.close()
conn.close()