import my_db_module

num = input("삭제할 대상의 번호 : ")

sql=f"delete from test where idx={num}"

dbObj = dbconn.DBConn('localhost','root','1234','Python')
conn = dbObj.DBConn()
if dbObj.exeQuery(sql):
    print("정상적으로 데이터를 삭제했습니다")
else:
    print("잠시 서버 장애가 발생했습니다.")
    
conn.comit()
conn.close()


rows=dbObf.readData(0)
for row in rows:
    for item in row:
        print(item, end="\t")
    print("")