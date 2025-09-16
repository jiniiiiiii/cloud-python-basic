import pymysql
'''
sql="""
SELECT * FROM test;
"""
# 데이터베이스 연결
conn = pymysql.connect(
    host = "localhost",
    user = "admin",
    password = "1234",
    database = "Python"
)
# 사실 이렇게 지정하면 안됨. 유출되는 순간 그냥 end.

# 2. 커서를 데이터베이스에 위치 
cursor = conn.cursor()

#3. 필요작업 수행 
# -> 서버한테 실행시키는거 x. 커서한테 실행시킴. 
resultConn = cursor.execute(sql)    # sql을 실행하고 나서 영향을 받은 행의 갯수를 반환
print(resultConn)

conn.commit()      # 실행 후 롤백 안됨. 
conn.close()
'''



# 좀 어렵게 
sql="""
SELECT idx, name, eng, math FROM test;
"""

def dbConn(host, user, password, database):
    conn = pymysql.connect(
        host = host,
        user = user,
        password = password,
        database = database
    )
    return conn

conn = dbConn("localhost", "root", "1234", "Python")

cursor = conn.cursor(pymysql.cursors.DictCursor)
# 넣을 수 있는 파라미터 값
#- pymysql.cursors.DictCursor   # 보통은 파라미터 값을 생략할 경우 list로 변환
cursor = conn.cursor(pymysql.cursors.DictCursor)
rs = cursor.execute(sql)


rows = cursor.fetchall()    # 모든 행 가져오기.  .fetchone() : 선택된 행 중 1개의 행 반환. 
# .fetchmay(size=n) : 선택된 행 중 n개의 행 반환
# cursor변수.메소드()     # 컬럼명이 키로, 데이터가 값으로 출력됨. 
'''
[{'idx': 1, 'name': '홍음', 'eng': 50, 'math': 70}, {'idx': 2, 'name': '홍', 'eng': 50, 'math': 70}, {'idx': 3, 'name': '억', 'eng': 150, 'math': 170}, {'idx': 4, 'name': '맴', 'eng': 20, 'math': 85}, {'idx': 5, 'name': '홍', 'eng': 50, 'math': 70}, {'idx': 6, 'name': '억', 'eng': 150, 'math': 170}, {'idx': 7, 'name': '맴', 'eng': 20, 'math': 85}]
'''


# rows = cursor.fetchone()    # 한행만 출력
# print(rows) 
'''
{'idx': 1, 'name': '홍음', 'eng': 50, 'math': 70}
'''

# rows = cursor.fetchmany(size=3)    # 지정된 숫자만큼 출력
# print(rows) 
'''
[{'idx': 2, 'name': '홍', 'eng': 50, 'math': 70}, {'idx': 3, 'name': '억', 'eng': 150, 'math': 170}, {'idx': 4, 'name': '맴', 'eng': 20, 'math': 85}]
'''



#출력
print("idx, name, eng, math")
for row in rows:
    for item in row:
        print([item][0])
        print(item, end="\t")
        
conn.close()