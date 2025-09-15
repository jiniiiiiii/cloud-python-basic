import json

# 리스트 안 딕셔너리
# JSON은 리스트+딕셔너리 같은거도 인정함. 
# *단, 데이터의 형식을 준수할 것. *
sample = """[
    {"name":"홍길동", "kor":10, "eng":20, "math":30},
    {
        "name":"["a","b"]", 
        "kor":10, 
        "eng":20, 
        "math":30
    },
    {"name":"홍길동", "kor":10, "eng":20, "math":30}
]"""
#print(type(sample)) # 데이터형 확인


# json 로드법 : json.loads("문자열") --> (리스트 or 딕셔너리 형태의)문자열을 리스트 or 딕셔너리로 변경시켜준다. 
# 기본적인 형태 안 맞춰져있으면 오류남. 
jsonData = json.loads(sample)
print(type(sample))     #str
print(type(jsonData))   #list -> 다시 문자로 바꾸려면 어떻게 해야할까?

# 리스트 or 딕셔너리를 -> str 변경
strData = json.dumps(jsonData)

print ("=== jsonData ===\n", jsonData, "\n")
print ("=== strData ===\n", strData, "\n")

'''
=== jsonData ===
 [{'name': '홍길동', 'kor': 10, 'eng': 20, 'math': 30}, {'name': '홍길동', 'kor': 10, 'eng': 20, 'math': 30}, {'name': '홍길동', 'kor': 10, 'eng': 20, 'math': 30}]

=== strData ===
 [{"name": "\ud64d\uae38\ub3d9", "kor": 10, "eng": 20, "math": 30}, {"name": "\ud64d\uae38\ub3d9", "kor": 10, "eng": 20, "math": 30}, {"name": "\ud64d\uae38\ub3d9", "kor": 10, "eng": 20, "math": 30}]
'''