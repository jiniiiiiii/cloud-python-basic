li = [
    [1,2,3,4],
    [5,6,7,8]
]

### 행번호 중심 ###
for i in range(len(li)):
    for j in range(len(li[i])):
        print(li[i][j], end="\t")
    print("")
print("#############################")


### data 중심 ###
# items = 변수명 (for문에서 i와 같음)
# 주석과 같이 사용해주면 인덱스 중심으로 사용 가능
# i = 0, j =0
for items in li:
    for items in items:
        print(items, end="\t")
        # j+= 1
    # i+=1
    print("")
    
    
    
'''
[출력]
1       2       3       4
5       6       7       8
#############################
1       2       3       4
5       6       7       8


'''